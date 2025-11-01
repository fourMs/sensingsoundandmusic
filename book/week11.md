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

[Computer audition](https://en.wikipedia.org/wiki/Computer_audition) or Machine listening is the practice of converting sound (music, speech, or environmental audio) into structured, usable information. At a high level this means capturing reliable audio, extracting features that reflect perceptual properties, detecting events and boundaries, mapping patterns to labels, modeling how sound evolves over time, combining cues into higher‑level interpretations, and presenting results in ways people or other systems can use.

It starts with robust **audio input and preprocessing**. Whether audio comes from microphones, interfaces, or files, common steps like resampling, DC removal, level normalization, denoising and de‑clicking make subsequent analysis more stable and fair across recordings. These operations increase signal‑to‑noise ratio, remove systematic artifacts (for example a low‑frequency hum), and ensure that feature extraction operates on comparable data.

**Feature extraction** converts waveforms into compact descriptors that are easier to work with and that better reflect hearing. Typical features include spectral measures (centroid, bandwidth), timbral representations (MFCCs), harmonic summaries (chroma, F0 contours), and temporal cues (onset strength, tempo). Choosing sensible parameters—window size, hop, number of mel bands, and normalization—shapes what information the model can access and directly affects downstream performance.

**Segmentation and event detection** locate meaningful boundaries and discrete events such as onsets, beats, section changes, or speech activity. Methods range from classic signal‑processing heuristics (peak‑picking on onset strength) to learned detectors and change‑point algorithms. Good segmentation makes indexing, alignment, and focused processing possible, and it is typically evaluated with event‑level metrics and tolerance windows.

**Classification and recognition map** features or learned representations to semantic labels—instrument types, genres, speech/music, or emotion—using models from SVMs and random forests to CNNs and transformers. Practical concerns include label quality, class imbalance, interpretability of decisions, and choosing metrics that fit the task (accuracy vs. precision/recall, per‑class performance, etc.). Start with simple baselines and increase model complexity as needed.

**Temporal modeling** captures sequence and context: rhythm, melody, phrasing and long‑range dependencies. Approaches include HMMs, RNNs/LSTMs, temporal CNNs and transformers; they improve tasks that rely on context (transcription, expressive timing, source activity), but introduce trade‑offs in latency, model size, and training data requirements. Decide early whether your application needs realtime responsiveness or offline, higher‑accuracy processing.

Finally, **higher‑level analysis** and outputs turn low‑level signals into actionable results: structure and form annotations, harmonic or mood estimates, symbolic exports (MIDI, MusicXML), visualizations, or interactive feedback (real‑time displays, haptic cues). Design outputs for the intended users—students, performers, researchers—pay attention to latency, provenance, and interoperability, and validate results with human‑grounded evaluation so outputs meaningfully reflect perception and musical practice.



### Resources

- Evaluation: use annotated datasets (e.g., [MIREX](https://www.music-ir.org/mirex/wiki/MIREX_HOME), [DCASE](https://dcase.community/)) and standard metrics — [precision & recall](https://en.wikipedia.org/wiki/Precision_and_recall), [F1 score](https://en.wikipedia.org/wiki/F1_score), and frame/segment-level measures (see [mir_eval](https://craffel.github.io/mir_eval/) for common implementations).


- Tools & libraries: e.g., [librosa](https://librosa.org/), [Essentia](https://essentia.upf.edu/), [madmom](https://github.com/CPJKU/madmom)


[PyTorch](https://pytorch.org/)/[TensorFlow](https://www.tensorflow.org/) for modeling.
- Datasets (examples): [GTZAN (genre)](http://marsyas.info/?q=content/gtzan-dataset-music-genre-classification), [MusicNet](https://homes.cs.washington.edu/~thickstn/musicnet.html), [IRMAS](https://www.upf.edu/web/mtg/irmas), [AudioSet](https://research.google.com/audioset/) — check licensing and usage terms before use.


## Music Information Retrieval

[Music Information Retrieval](https://en.wikipedia.org/wiki/Music_information_retrieval) (MIR) can be seen as a specialized form of machine listening, aimed at extracting structured, actionable information from musical audio and related data. MIR combines signal processing, machine learning, music theory, and human-centred evaluation to support tasks such as metadata extraction, music search, analysis, learning, and interactive applications. The following sections describe core MIR tasks, typical approaches, and practical considerations for building and evaluating systems.

### Overview
MIR tasks operate at different levels of abstraction: low-level signal descriptors (spectral, temporal, harmonic), mid-level events (onsets, beats, notes), and high-level semantics (genre, mood, structure). Effective MIR pipelines often combine careful preprocessing, feature extraction, event detection, and modeling (classical or learned), with task-specific evaluation and human validation.

### Classification
Classification maps extracted features or learned representations to categorical labels such as genre, instrument, or mood. Approaches range from classical machine learning (e.g., [support vector machines](https://en.wikipedia.org/wiki/Support-vector_machine), [random forests](https://en.wikipedia.org/wiki/Random_forest)) on hand-crafted features ([MFCCs](https://en.wikipedia.org/wiki/Mel-frequency_cepstrum), [chroma](https://en.wikipedia.org/wiki/Chroma_feature)) to deep models ([CNNs](https://en.wikipedia.org/wiki/Convolutional_neural_network), [transformers](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model))) trained end-to-end on [spectrograms](https://en.wikipedia.org/wiki/Spectrogram) or learned representations ([representation learning](https://en.wikipedia.org/wiki/Representation_learning)). Key issues include [class imbalance](https://en.wikipedia.org/wiki/Imbalanced_dataset), [domain mismatch / domain adaptation](https://en.wikipedia.org/wiki/Domain_adaptation) between datasets and deployment audio, and the choice of metrics (per-class [precision & recall](https://en.wikipedia.org/wiki/Precision_and_recall), macro vs. micro averaging). Start with simple baselines and use calibration ([calibration (statistics)](https://en.wikipedia.org/wiki/Calibration_(statistics))), interpretability tools ([interpretability](https://en.wikipedia.org/wiki/Interpretability)), and uncertainty estimation ([uncertainty quantification](https://en.wikipedia.org/wiki/Uncertainty_quantification)) for production systems.

### Recommendation
Recommendation systems use MIR outputs and user interaction data to suggest relevant music. Content-based methods leverage extracted audio features and metadata; collaborative filtering uses user-item interactions; hybrid approaches combine both. Practical considerations include cold-start for new tracks/users, fairness and diversity in recommendations, privacy of user data, and scalable retrieval/indexing for large music catalogs.

### Source Separation
Source separation isolates individual instruments or voices from a mixed audio signal. Methods include traditional matrix factorization and spatial filtering, as well as modern deep-learning approaches (U‑Nets, Conv‑TasNet, time-domain separation). Evaluation commonly uses signal‑level metrics (SDR, SIR, SAR) and perceptual listening tests. Separation quality depends strongly on training data diversity, labeling fidelity, and mixture complexity; post-processing and masking heuristics can improve perceptual results.

![Source separation](https://upload.wikimedia.org/wikipedia/commons/c/c3/Polyphonic_note_separation_%26_manipulation.jpg)

*An example of polyphonic note separation ([Wikipedia](https://en.wikipedia.org/wiki/Signal_separation#/media/File:Polyphonic_note_separation_&_manipulation.jpg)).*

### Transcription
Automatic transcription converts audio into symbolic representations such as MIDI or MusicXML. Tasks range from monophonic pitch tracking to polyphonic multi-instrument transcription. Techniques include spectral analysis and onset/pitch detection heuristics, probabilistic sequence models, and end-to-end deep architectures with sequence losses (CTC, seq2seq). Challenges include polyphony, expressive timing, tuning deviations, and evaluating alignment accuracy versus symbolic correctness.

### Question‑Answering and Semantic Retrieval
Audio-based question‑answering and semantic retrieval combine MIR with natural language interfaces: queries like “which song has a trumpet solo?” or “find tracks with a fast tempo and major mode.” Systems integrate audio tagging, metadata, lyrics, and semantic embeddings to match queries to audio segments. Robustness depends on accurate multimodal indexing, interpretable tag sets, and careful mapping between user language and model labels.

### Segmentation and Structure Analysis
Segmentation partitions tracks into meaningful regions (intro, verse, chorus) or detects events (sections, transitions). Approaches use novelty detection on self-similarity matrices, supervised boundary detectors, or learned representations for structural segmentation. Applications include navigation, summarization, and alignment. Evaluation typically uses boundary precision/recall with tolerance windows and structural similarity measures.

### Feature Extraction
Feature extraction produces compact descriptors that capture perceptual or musical properties: spectral features (centroid, bandwidth), timbral features (MFCCs), harmonic descriptors (chroma, pitch contours), and temporal features (onset strength, tempo). Choose parameters (window length, hop size, mel bands) to match the temporal and spectral resolution required by the task. Normalization, augmentation, and invariant representations (e.g., pitch- or tempo-invariant features) improve robustness.

### Evaluation, Datasets, and Benchmarks
Use standardized datasets and metrics appropriate to each task (e.g., GTZAN for genre with caveats, MusicNet for transcription, DSD100 for separation). Combine objective metrics with perceptual evaluations when possible. Always check dataset licensing and biases, and report per-class and aggregate metrics to reveal failure modes.

### Practical Considerations
- Latency and deployment constraints: decide realtime vs offline trade-offs early.  
- Data quality: ensure annotations are consistent and representative.  
- Augmentation and robustness: apply pitch‑shift, time‑stretch, and noise to reduce overfitting.  
- Ethics & licensing: respect copyright, user privacy, and address demographic or cultural biases in training data.

Together these components form a practical MIR workflow: define the task and metrics, collect and preprocess data, select appropriate features and models, evaluate with relevant benchmarks and human studies, and iterate towards robust, explainable systems.

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
