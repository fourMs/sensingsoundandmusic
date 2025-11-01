---
title: "Week 11: Machine Listening"
subtitle: "Audio analysis, feature extraction, and physiological response measurement"
description: "A practical overview of machine listening: techniques for audio input and preprocessing, feature extraction, segmentation, classification, temporal modeling, and higher‑level analysis. Covers tools, datasets, evaluation metrics, and workflows for both realtime and offline systems, with examples and applications in music and speech."
exports:
  - format: pdf
---

This week we will explore machine listening, a field where music psychology meets music technology to turn sound into structured information. We will survey the full signal-to-symbol pipeline—from capture and preprocessing through feature extraction, segmentation, classification, and temporal modelling—and emphasise how perceptual principles inform algorithm design and evaluation. 

Learning goals
- Understand common preprocessing steps and why they matter for downstream analysis.
- Be able to extract and interpret core audio features (MFCCs, chroma, spectral descriptors, onsets, F0).
- Compare segmentation, classification, source separation, and transcription approaches and choose appropriate evaluation metrics.
- Appreciate practical constraints (latency, dataset bias, licensing) and ethical considerations when working with audio and user data.

Hands-on activities
- Guided notebooks: feature extraction with librosa and basic visualization (spectrograms, chroma, onset plots).
- Small projects: (a) implement an onset detector and evaluate it on sample recordings; (b) train a simple instrument/genre classifier using a provided dataset; (c) prototype a realtime pitch-monitoring visualizer.
- Experiments with augmentation and robustness: time-stretch, pitch-shift, noise injection, and their effects on model performance.

Tools & resources
- Recommended libraries: librosa, torchaudio, PyTorch/TensorFlow, Essentia, madmom.
- Example datasets for experiments: GTZAN, MusicNet, IRMAS, AudioSet (use according to licensing).
- Further reading and demos will be provided in the course notes and linked notebooks.


## Machine Listening

Machine listening is about enabling systems to perceive and interpret sound—music, speech, and environmental audio—by turning waveforms into structured, actionable representations.

### Core components
1. Audio input & preprocessing  
    - What it does: capture audio (microphones, files) and clean/standardize it (denoising, resampling, normalization).  
    - Why it matters: improves downstream reliability and reduces noise-induced errors.  
    - Example: removing background hum from a concert recording.

2. Feature extraction  
    - What it does: convert audio into descriptors (spectral, temporal, pitch/harmonic).  
    - Common features: MFCCs, chroma, spectral centroid, onset strength, tempo, F0.  
    - Why it matters: features are the representation models use to learn and infer.  
    - Example: extracting pitch contours to evaluate intonation.

3. Segmentation & event detection  
    - What it does: locate boundaries and discrete events (notes, beats, scene changes).  
    - Why it matters: enables precise indexing and targeted analysis.  
    - Example: detecting note onsets in a piano performance.

4. Classification & recognition  
    - What it does: assign labels to audio (instruments, genre, speech/music, emotions).  
    - Why it matters: provides semantic understanding for search, recommendation, and interaction.  
    - Example: identifying violins in an orchestral mix.

5. Temporal modeling  
    - What it does: model sequential structure (rhythm, melody, transitions).  
    - Typical methods: HMMs, RNNs/LSTMs, temporal CNNs, transformers.  
    - Why it matters: captures dependencies across time essential to music and speech.

6. Higher-level analysis  
    - What it does: infer structure, form, affect, or intent from audio.  
    - Why it matters: bridges low-level signal processing with perceptual and musical meaning.  
    - Example: estimating mood from a film score.

7. Output & interaction  
    - What it does: present results as visualizations, MIDI, transcriptions, or interactive feedback.  
    - Why it matters: makes analyses useful for education, production, and research.  
    - Example: real-time pitch-monitoring visualizer for singers.

### Practical notes
- Evaluation: use annotated datasets and metrics (precision/recall, F1, frame/segment accuracy).  
- Tools & libraries: e.g., librosa, Essentia, madmom, PyTorch/TensorFlow for modeling.  
- Datasets (examples): GTZAN, MusicNet, IRMAS, AudioSet.

### Interdisciplinary connections
- Musicology: automated analysis of style and historical recordings.  
- Music psychology: linking features to perception and cognition.  
- Music technology: tools for composition, performance, education, and accessibility.

## Music Information Retrieval

Information retrieval in machine listening involves extracting meaningful information from audio data. Key areas include:

- **Classification**: This involves categorizing audio into predefined classes, such as:
    - [Genre](https://en.wikipedia.org/wiki/Music_genre)
    - [Instruments](https://en.wikipedia.org/wiki/Musical_instrument)
    - [Mood](https://en.wikipedia.org/wiki/Mood_(psychology))
- **Recommendation**: Systems that suggest music or audio content based on user preferences. Learn more about [recommender systems](https://en.wikipedia.org/wiki/Recommender_system).
- **Source Separation**: The process of isolating individual sound sources from a mixture. See [source separation](https://en.wikipedia.org/wiki/Audio_signal_processing#Source_separation).
- **Transcription**: Converting audio into symbolic representations like sheet music. Learn about [music transcription](https://en.wikipedia.org/wiki/Music_transcription).
- **Question-Answering**: Systems that answer questions based on audio content.
- **Segmentation**: Dividing audio into meaningful segments, such as verses or choruses in music.
- **Feature Extraction**: Extracting characteristics like pitch, tempo, or timbre from audio. See [audio feature extraction](https://en.wikipedia.org/wiki/Feature_extraction).

### Data

Machine listening relies on various types of data:

- **Symbolic Data**: Representations like [MIDI](https://en.wikipedia.org/wiki/MIDI) and [MusicXML](https://en.wikipedia.org/wiki/MusicXML).
- **Subsymbolic Data**: Includes raw audio, video, and sensor data.
- **Metadata**: Information about the audio, such as artist or album details. Learn about [metadata](https://en.wikipedia.org/wiki/Metadata).
- **Paradata**: Data about the process of data collection or analysis.
- **User Data**: Information about user interactions and preferences.


### Artificial Intelligence (AI)

AI techniques in machine listening span a spectrum from hand-crafted rules to large, data-driven models. Below is a concise taxonomy with practical notes and examples.

- Rule-based systems
    - What: deterministic heuristics and signal-processing rules (thresholds, peak-picking, spectral heuristics).
    - When useful: lightweight, interpretable, low-latency tasks (onset picking, simple voice activity detection).
    - Pros/cons: fast and explainable but brittle to noise and domain shifts.

- Learning-based systems
    - Supervised classical ML: feature-to-label models (SVMs, random forests) using MFCCs, chroma, etc. Good for small data and interpretable features.
    - Deep learning: end-to-end or feature-based models (CNNs for timbre/scene classification, RNNs/LSTMs for temporal modelling, transformers for long-range context).
    - Self-/semi-supervised learning: pretraining (contrastive or predictive) on large unlabeled audio, then fine-tuning for downstream tasks—helps when labels are scarce.
    - Examples: CNN instrument classifiers, U‑Net/Conv‑TasNet for source separation, seq2seq/CTC models for automatic transcription.

- Hybrid approaches
    - Combine signal-processing priors with learned components (e.g., learned post-filtering of spectrograms, rule-based event grouping on ML-detected onsets).
    - Balance interpretability, performance, and data requirements.

- Practical considerations
    - Data: annotation quality, class balance, synthetic augmentation (pitch-shift, time-stretch, noise), and domain mismatch.
    - Evaluation: choose metrics per task (precision/recall/F1, SDR/SIR for separation, frame/segment accuracy for transcription).
    - Deployment: model size, latency (realtime vs offline), hardware constraints, and model update strategy.
    - Robustness & ethics: guard against bias, adversarial/noisy inputs, and respect data licensing.

- Tools & libraries (examples)
    - Feature & DSP: [librosa](https://librosa.org/), [madmom](https://github.com/CPJKU/madmom), [Essentia](https://essentia.upf.edu/)
    - Modeling & infra: [PyTorch](https://pytorch.org/), [TensorFlow](https://www.tensorflow.org/), [torchaudio](https://pytorch.org/audio/), [Hugging Face](https://huggingface.co/)
    - Task-specific: [Asteroid (source separation)](https://github.com/asteroid-team/asteroid), [nnAudio](https://github.com/KinWaiCheuk/nnAudio), [pretrained audio transformers (Hugging Face models)](https://huggingface.co/models?pipeline_tag=audio-classification)

- Typical workflow
    1. Define task and metrics.
    2. Collect/annotate/augment data.
    3. Choose baseline (rule-based or simple ML), then iterate with deeper models.
    4. Validate on held-out data, optimize for latency/robustness, deploy and monitor.

This framing helps pick appropriate techniques given data availability, latency needs, and interpretability requirements.

### Time

Machine listening systems can operate in different time modes:

- **Realtime**: Systems that process audio as it is received, such as [online systems](https://en.wikipedia.org/wiki/Real-time_computing).
- **Non-Realtime**: Systems that process audio after it has been recorded, such as [offline systems](https://en.wikipedia.org/wiki/Batch_processing).




```{note}
SonicVisualiser
```
