const toggleCameraBtn = document.getElementById("toggleCameraBtn");
const cameraVideo = document.getElementById("cameraVideo");
const viewCanvas = document.getElementById("viewCanvas");
const viewCtx = viewCanvas ? viewCanvas.getContext("2d", { willReadFrequently: true }) : null;
const videogramCanvas = document.getElementById("videogramCanvas");
const videogramCanvasVert = document.getElementById("videogramCanvasVert");
const selfSimCanvas = document.getElementById("selfSimCanvas");
const selfSimCtx = selfSimCanvas ? selfSimCanvas.getContext("2d", { willReadFrequently: true }) : null;
const videoModeTitle = document.getElementById("videoModeTitle");
const vertGramTitle = document.getElementById("vertGramTitle");
const horizGramTitle = document.getElementById("horizGramTitle");
const mirrorBtn = document.getElementById("mirrorBtn");
const diffBtn = document.getElementById("diffBtn");
let frameDifferencing = false;
let prevFrame = null;
// --- Frame differencing buffer for temporal averaging ---
const FRAME_DIFF_AVG_COUNT = 4; // Number of diffs to average
let diffBuffer = [];

function resetDiffBuffer() {
  diffBuffer = [];
}

function syncModeLabels() {
  if (videoModeTitle) {
    videoModeTitle.textContent = frameDifferencing ? "Motion video" : "Regular video";
  }
  if (vertGramTitle) {
    vertGramTitle.textContent = frameDifferencing ? "Motiongram (Vertical Avg)" : "Videogram (Vertical Avg)";
  }
  if (horizGramTitle) {
    horizGramTitle.textContent = frameDifferencing ? "Motiongram (Horizontal Avg)" : "Videogram (Horizontal Avg)";
  }
}

const diffThreshold = document.getElementById("diffThreshold");
const diffThresholdValue = document.getElementById("diffThresholdValue");
const normalizeBtn = document.getElementById("normalizeBtn");
let threshold = 0;
let normalize = true;
if (diffThreshold) {
  diffThreshold.addEventListener("input", (e) => {
    threshold = Number(e.target.value);
    if (diffThresholdValue) diffThresholdValue.textContent = threshold;
  });
  threshold = Number(diffThreshold.value);
  if (diffThresholdValue) diffThresholdValue.textContent = threshold;
}
if (normalizeBtn) {
  normalize = normalizeBtn.getAttribute("aria-pressed") === "true";
  normalizeBtn.classList.toggle("is-active", normalize);
  normalizeBtn.addEventListener("click", () => {
    normalize = !normalize;
    normalizeBtn.setAttribute("aria-pressed", String(normalize));
    normalizeBtn.classList.toggle("is-active", normalize);
  });
}

if (diffBtn) {
  frameDifferencing = diffBtn.getAttribute("aria-pressed") === "true";
  diffBtn.classList.toggle("is-active", frameDifferencing);
  syncModeLabels();
  diffBtn.addEventListener("click", () => {
    frameDifferencing = !frameDifferencing;
    diffBtn.setAttribute("aria-pressed", String(frameDifferencing));
    diffBtn.classList.toggle("is-active", frameDifferencing);
    prevFrame = null; // Reset on toggle
    resetDiffBuffer();
    resetSSM();
    syncModeLabels();
  });
}

const videogramCtx = videogramCanvas.getContext("2d", { willReadFrequently: true });
const videogramCtxVert = videogramCanvasVert.getContext("2d", { willReadFrequently: true });
const sampleCanvas = document.createElement("canvas");
const sampleCtx = sampleCanvas.getContext("2d", { willReadFrequently: true });



let stream = null;
let rafId = null;
let processing = false;
let mirrored = false;
const videoWidth = 400;
const videoHeight = 400;
const duration = 400;
let horizBuffer = null;
let vertBuffer = null;

// --- Self-similarity matrix (SSM) ---
// Keep this independent of `duration` for performance (N^2 cost).
const SSM_SIZE = 256;
const SSM_FEATURE_W = 24;
const SSM_FEATURE_H = 24;
const SSM_FEATURE_DIM = SSM_FEATURE_W * SSM_FEATURE_H;
const SSM_UPDATE_EVERY_N_FRAMES = 6;
let ssmFeatures = [];
let ssmFrameCounter = 0;
const ssmSmallCanvas = document.createElement("canvas");
ssmSmallCanvas.width = SSM_SIZE;
ssmSmallCanvas.height = SSM_SIZE;
const ssmSmallCtx = ssmSmallCanvas.getContext("2d", { willReadFrequently: true });

function updateStatus(message) {}

function resetSSM() {
  ssmFeatures = [];
  ssmFrameCounter = 0;
  if (ssmSmallCtx) ssmSmallCtx.clearRect(0, 0, SSM_SIZE, SSM_SIZE);
  if (selfSimCtx && selfSimCanvas) selfSimCtx.clearRect(0, 0, selfSimCanvas.width, selfSimCanvas.height);
}

function extractSSMFeature(rgbOrGrayData, w, h) {
  // Downsample to a small grid and normalize for cosine similarity.
  const feat = new Float32Array(SSM_FEATURE_DIM);
  let k = 0;

  for (let gy = 0; gy < SSM_FEATURE_H; gy++) {
    const y = Math.min(h - 1, Math.floor((gy + 0.5) * (h / SSM_FEATURE_H)));
    for (let gx = 0; gx < SSM_FEATURE_W; gx++) {
      const x = Math.min(w - 1, Math.floor((gx + 0.5) * (w / SSM_FEATURE_W)));
      const idx = (y * w + x) * 4;
      // Use grayscale intensity.
      feat[k++] = (rgbOrGrayData[idx] + rgbOrGrayData[idx + 1] + rgbOrGrayData[idx + 2]) / (3 * 255);
    }
  }

  // Zero-mean + unit-norm for more informative cosine similarity.
  let mean = 0;
  for (let i = 0; i < feat.length; i++) mean += feat[i];
  mean /= feat.length;

  let norm = 0;
  for (let i = 0; i < feat.length; i++) {
    const v = feat[i] - mean;
    feat[i] = v;
    norm += v * v;
  }
  norm = Math.sqrt(norm) || 1;
  for (let i = 0; i < feat.length; i++) feat[i] /= norm;

  return feat;
}

function renderSSM() {
  if (!selfSimCtx || !selfSimCanvas || !ssmSmallCtx) return;

  const n = ssmFeatures.length;
  if (n === 0) return;

  const out = new Uint8ClampedArray(SSM_SIZE * SSM_SIZE * 4);
  const size = SSM_SIZE;

  // Map features (most recent first) into an NxN similarity image.
  for (let y = 0; y < size; y++) {
    const iy = Math.floor((y / size) * n);
    const fy = ssmFeatures[iy];
    for (let x = 0; x < size; x++) {
      const ix = Math.floor((x / size) * n);
      const fx = ssmFeatures[ix];

      let dot = 0;
      for (let i = 0; i < SSM_FEATURE_DIM; i++) dot += fx[i] * fy[i];
      // dot is in [-1, 1]; map to [0, 255]
      const v = 255 - Math.max(0, Math.min(255, Math.round(((dot + 1) / 2) * 255)));

      const o = (y * size + x) * 4;
      out[o] = v;
      out[o + 1] = v;
      out[o + 2] = v;
      out[o + 3] = 255;
    }
  }

  ssmSmallCtx.putImageData(new ImageData(out, SSM_SIZE, SSM_SIZE), 0, 0);
  selfSimCtx.imageSmoothingEnabled = false;
  selfSimCtx.clearRect(0, 0, selfSimCanvas.width, selfSimCanvas.height);
  selfSimCtx.drawImage(ssmSmallCanvas, 0, 0, selfSimCanvas.width, selfSimCanvas.height);
}

function drawVideoCover(ctx, videoEl, w, h, mirror) {
  // Draw the current video frame into a fixed WxH box using "cover"
  // (center-crop) so the live view is a square crop.
  const vw = videoEl.videoWidth || w;
  const vh = videoEl.videoHeight || h;
  const scale = Math.max(w / vw, h / vh);
  const dw = Math.round(vw * scale);
  const dh = Math.round(vh * scale);
  const dx = Math.floor((w - dw) / 2);
  const dy = Math.floor((h - dh) / 2);

  ctx.save();
  ctx.setTransform(1, 0, 0, 1, 0, 0);
  ctx.clearRect(0, 0, w, h);

  if (mirror) {
    ctx.translate(w, 0);
    ctx.scale(-1, 1);
    ctx.drawImage(videoEl, w - dx - dw, dy, dw, dh);
  } else {
    ctx.drawImage(videoEl, dx, dy, dw, dh);
  }
  ctx.restore();
}

function setButtons(isStreaming) {
  toggleCameraBtn.textContent = isStreaming ? "Stop Camera" : "Start Camera";
  toggleCameraBtn.classList.toggle("is-active", isStreaming);
  toggleCameraBtn.setAttribute("aria-pressed", String(isStreaming));
}

function applySampleSize() {
  sampleCanvas.width = videoWidth;
  sampleCanvas.height = videoHeight;

  // Horizontal videogram (row-averaged): width = videoWidth, height = duration (square)
  videogramCanvas.width = videoWidth;
  videogramCanvas.height = duration;
  horizBuffer = new Uint8ClampedArray(videoWidth * duration * 4);
  videogramCtx.clearRect(0, 0, videogramCanvas.width, videogramCanvas.height);

  // Vertical videogram (column-averaged): width = duration, height = videoHeight (square)
  videogramCanvasVert.width = duration;
  videogramCanvasVert.height = videoHeight;
  vertBuffer = new Uint8ClampedArray(duration * videoHeight * 4);
  videogramCtxVert.clearRect(0, 0, videogramCanvasVert.width, videogramCanvasVert.height);
}



function drawVideogramFrame() {
  if (!processing || cameraVideo.readyState < HTMLMediaElement.HAVE_CURRENT_DATA) {
    rafId = requestAnimationFrame(drawVideogramFrame);
    return;
  }

  // Draw the frame into our fixed processing resolution using "contain",
  // so we can display a consistent 480x480 crop in all views.
  drawVideoCover(sampleCtx, cameraVideo, videoWidth, videoHeight, mirrored);

  let frame = sampleCtx.getImageData(0, 0, videoWidth, videoHeight);
  let data = frame.data;
  const rawData = data;

  // Frame differencing with threshold, normalization, and temporal averaging
  let diffData = data;
  if (frameDifferencing) {
    if (prevFrame) {
      let prevData = prevFrame.data;
      let rawDiff = new Uint8ClampedArray(data.length);
      let maxDiff = 0;
      for (let i = 0; i < data.length; i += 4) {
        // Compute per-pixel difference (grayscale)
        const dr = Math.abs(data[i] - prevData[i]);
        const dg = Math.abs(data[i + 1] - prevData[i + 1]);
        const db = Math.abs(data[i + 2] - prevData[i + 2]);
        let diff = (dr + dg + db) / 3;
        if (diff > maxDiff) maxDiff = diff;
        rawDiff[i] = rawDiff[i + 1] = rawDiff[i + 2] = diff;
        rawDiff[i + 3] = 255;
      }
      // Add to buffer
      diffBuffer.push(rawDiff);
      if (diffBuffer.length > FRAME_DIFF_AVG_COUNT) diffBuffer.shift();
      // Average buffer
      diffData = new Uint8ClampedArray(data.length);
      for (let i = 0; i < data.length; i += 4) {
        let sum = 0;
        for (let b = 0; b < diffBuffer.length; ++b) {
          sum += diffBuffer[b][i];
        }
        let avg = sum / diffBuffer.length;
        // Threshold
        avg = avg >= threshold ? avg : 0;
        diffData[i] = diffData[i + 1] = diffData[i + 2] = avg;
        diffData[i + 3] = 255;
      }
      // Normalize if enabled
      if (normalize) {
        let maxVal = 0;
        for (let i = 0; i < diffData.length; i += 4) {
          if (diffData[i] > maxVal) maxVal = diffData[i];
        }
        if (maxVal > 0) {
          for (let i = 0; i < diffData.length; i += 4) {
            diffData[i] = diffData[i + 1] = diffData[i + 2] = Math.round((diffData[i] / maxVal) * 255);
          }
        }
      }
    }
    // Always store the original frame for next diff
    prevFrame = new ImageData(new Uint8ClampedArray(data), videoWidth, videoHeight);
  } else {
    prevFrame = new ImageData(new Uint8ClampedArray(data), videoWidth, videoHeight);
    diffData = data;
    diffBuffer = [];
  }

  // Draw the square live view (camera or motion) into the visible canvas.
  if (viewCtx && viewCanvas) {
    if (frameDifferencing && prevFrame) {
      viewCtx.putImageData(new ImageData(diffData, videoWidth, videoHeight), 0, 0);
    } else {
      viewCtx.putImageData(frame, 0, 0);
    }
  }

  // --- Self-similarity update (use same data source as videograms) ---
  if (selfSimCtx && selfSimCanvas) {
    // When frame differencing is off, build the SSM from the original video.
    // When on, build it from the motion/difference image.
    const ssmSource = frameDifferencing ? diffData : rawData;
    const feat = extractSSMFeature(ssmSource, videoWidth, videoHeight);
    ssmFeatures.unshift(feat);
    if (ssmFeatures.length > SSM_SIZE) ssmFeatures.pop();

    ssmFrameCounter++;
    if (ssmFrameCounter % SSM_UPDATE_EVERY_N_FRAMES === 0) {
      renderSSM();
    }
  }


  // Horizontal videogram (row-averaged)
  const averagedRow = new Uint8ClampedArray(videoWidth * 4);
  for (let x = 0; x < videoWidth; x += 1) {
    let r = 0, g = 0, b = 0;
    for (let y = 0; y < videoHeight; y += 1) {
      const idx = (y * videoWidth + x) * 4;
      r += diffData[idx];
      g += diffData[idx + 1];
      b += diffData[idx + 2];
    }
    const pixelIndex = x * 4;
    const scale = videoHeight;
    averagedRow[pixelIndex] = Math.round(r / scale);
    averagedRow[pixelIndex + 1] = Math.round(g / scale);
    averagedRow[pixelIndex + 2] = Math.round(b / scale);
    averagedRow[pixelIndex + 3] = 255;
  }
  // Scroll buffer down and add new row at the top (reverse direction)
  horizBuffer.copyWithin(videoWidth * 4, 0);
  horizBuffer.set(averagedRow, 0);
  // Draw buffer to canvas, mirrored if needed
  const horizImage = new ImageData(new Uint8ClampedArray(horizBuffer), videoWidth, duration);
  if (mirrored) {
    videogramCtx.save();
    videogramCtx.translate(videoWidth, 0);
    videogramCtx.scale(-1, 1);
    videogramCtx.putImageData(horizImage, 0, 0);
    videogramCtx.restore();
  } else {
    videogramCtx.putImageData(horizImage, 0, 0);
  }


  // Vertical videogram (column-averaged)
  const averagedCol = new Uint8ClampedArray(videoHeight * 4);
  for (let y = 0; y < videoHeight; y += 1) {
    let r = 0, g = 0, b = 0;
    for (let x = 0; x < videoWidth; x += 1) {
      const idx = (y * videoWidth + x) * 4;
      r += diffData[idx];
      g += diffData[idx + 1];
      b += diffData[idx + 2];
    }
    const pixelIndex = y * 4;
    const scale = videoWidth;
    averagedCol[pixelIndex] = Math.round(r / scale);
    averagedCol[pixelIndex + 1] = Math.round(g / scale);
    averagedCol[pixelIndex + 2] = Math.round(b / scale);
    averagedCol[pixelIndex + 3] = 255;
  }
  // Scroll buffer right and add new column at the left (reverse direction)
  for (let y = 0; y < videoHeight; y++) {
    vertBuffer.copyWithin(y * duration * 4 + 4, y * duration * 4, (y + 1) * duration * 4 - 4);
    vertBuffer.set(averagedCol.slice(y * 4, y * 4 + 4), y * duration * 4);
  }
  // Draw buffer to canvas
  const vertImage = new ImageData(new Uint8ClampedArray(vertBuffer), duration, videoHeight);
  videogramCtxVert.putImageData(vertImage, 0, 0);

  rafId = requestAnimationFrame(drawVideogramFrame);
}

async function startCamera() {
  if (processing) {
    return;
  }

  try {
    resetSSM();
    stream = await navigator.mediaDevices.getUserMedia({
      video: {
        width: { ideal: 1280 },
        height: { ideal: 720 },
        facingMode: "user"
      },
      audio: false
    });

    cameraVideo.srcObject = stream;
    await cameraVideo.play();

    // After video is playing, update the vertical videogram canvas width and height to fixed 320px width
    setTimeout(() => {
      applySampleSize();
    }, 100);

    processing = true;
    setButtons(true);
    drawVideogramFrame();
  } catch (error) {
    console.error(error);
  }
}

function stopCamera() {
  processing = false;

  if (rafId !== null) {
    cancelAnimationFrame(rafId);
    rafId = null;
  }

  if (stream) {
    stream.getTracks().forEach((track) => track.stop());
    stream = null;
  }

  cameraVideo.srcObject = null;
  setButtons(false);
  resetSSM();
}



if (mirrorBtn) {
  mirrored = mirrorBtn.getAttribute("aria-pressed") === "true";
  mirrorBtn.classList.toggle("is-active", mirrored);
  mirrorBtn.addEventListener("click", () => {
    mirrored = !mirrored;
    mirrorBtn.setAttribute("aria-pressed", String(mirrored));
    mirrorBtn.classList.toggle("is-active", mirrored);
  });
}

toggleCameraBtn.addEventListener("click", () => {
  if (processing) {
    stopCamera();
  } else {
    startCamera();
  }
});

applySampleSize();
