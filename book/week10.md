---
title: "Week 10: Physiology"
subtitle: "Physiology and measurement of bodily responses to music"
description: "Physiology and measurement of bodily responses to music: skin conductance, cardiac dynamics (heart rate, heart‑rate variability, synchronization), respiration effects, wearable monitoring methods (e.g., Equivital), and representative empirical studies and citations."
exports:
  - format: pdf
---

This week we explore how the body responds to sound and music, from fast autonomic reactions to slower respiratory and motor changes. We will examine physiological markers (heart rate and heart‑rate variability, skin conductance, respiration, blood pressure, and vocal/EGG measures), the physiological mechanisms that produce them (sympathetic/parasympathetic balance, entrainment, respiration–voice interactions), and methodological issues in measuring these signals in laboratory and concert settings.


## Physiological Reactions to Music

### Autonomic mechanisms: sympathetic vs. parasympathetic

The autonomic nervous system (ANS) comprises two primary branches with complementary roles: the sympathetic nervous system, which mobilizes resources for action and physiological arousal (see [sympathetic nervous system](https://en.wikipedia.org/wiki/Sympathetic_nervous_system)), and the parasympathetic nervous system, which promotes restoration and calm (see [parasympathetic nervous system](https://en.wikipedia.org/wiki/Parasympathetic_nervous_system)). For an overview of the system as a whole, see [autonomic nervous system](https://en.wikipedia.org/wiki/Autonomic_nervous_system). Sympathetic activation typically increases heart rate and contractility, raises blood pressure, elevates sweat‑gland activity (skin conductance), and redistributes blood flow toward skeletal muscle; parasympathetic (largely vagal) influence slows heart rate, supports digestion, and favors low‑arousal states via the vagus nerve ([vagus nerve](https://en.wikipedia.org/wiki/Vagus_nerve)).

At the physiological and biochemical level, sympathetic effects are mediated primarily by noradrenergic signaling (norepinephrine; [norepinephrine](https://en.wikipedia.org/wiki/Norepinephrine)) and are reflected in measures such as increased heart rate ([heart rate](https://en.wikipedia.org/wiki/Heart_rate)), reduced short‑term heart‑rate variability (HRV; [heart rate variability](https://en.wikipedia.org/wiki/Heart_rate_variability)), elevated skin conductance level (SCL; [galvanic skin response](https://en.wikipedia.org/wiki/Galvanic_skin_response)), and higher blood pressure ([blood pressure](https://en.wikipedia.org/wiki/Blood_pressure)). Parasympathetic or vagal influence manifests as decreased heart rate, larger respiratory‑sinus‑arrhythmia (RSA; [respiratory sinus arrhythmia](https://en.wikipedia.org/wiki/Respiratory_sinus_arrhythmia)) and increased high‑frequency components of HRV (see HRV link above), which together index rapid vagal modulation of cardiac timing.

These two branches also differ in temporal dynamics: sympathetic adjustments often unfold over seconds to minutes as hormones and slow neural pathways modulate peripheral organs, whereas vagal (parasympathetic) effects can operate on a beat‑to‑beat timescale, producing millisecond‑level modulation of the cardiac cycle detectable in ECG and HRV metrics. For measurement, concurrent recording of ECG, respiration, and skin conductance helps dissociate fast vagal influences from slower sympathetic and metabolic changes.

### How music shifts autonomic balance
Acoustic features such as tempo, loudness, timbre and spectral balance strongly bias autonomic state: slow tempi, soft dynamics, smooth timbres and lower spectral centroid tend to promote parasympathetic dominance (reduced heart rate, increased HRV, and lower tonic and phasic skin conductance), whereas fast tempi, greater loudness, sharp attacks and high‑energy spectral content favor sympathetic activation (elevated heart rate, reduced HRV, and higher SCL).

Rhythmic regularity and tempo provide powerful entrainment cues for respiration and cardiac timing. Steady, slower musical pulses can slow breathing and enhance respiratory sinus arrhythmia (RSA), producing beat‑to‑beat vagal modulation of the heart, while faster rhythms typically accelerate respiration and heart rate and can reduce vagal indices; entrainment strength depends on rhythmic salience and the listener’s attentional engagement.

Emotional appraisal of music contributes independently via valence and arousal pathways: music experienced as relaxing or pleasant biases toward parasympathetic engagement, whereas highly arousing, suspenseful, or threatening passages drive sympathetic responses. Temporal dynamics matter too—brief surprising events often elicit phasic sympathetic bursts (SCRs) superimposed on tonic autonomic trends set by overall valence and arousal.

Cognitive and social context modulate these sensory effects. Attention, expectation, memory and surprise change the magnitude and timing of autonomic responses, and live or collective settings (group singing, concerts) amplify shared autonomic dynamics and increase inter‑subject synchronization through social engagement and multimodal cues.

Motor and vocal activity interact with purely auditory influences: movement, dancing or singing increases metabolic demand and alters respiration, which in turn shifts heart rate and HRV independent of acoustic features. Experimental designs should therefore separate passive listening from active, movement‑based conditions or explicitly model motor contributions.

Individual differences and situational factors determine response variability. Baseline autonomic tone (vagal tone), musical training, familiarity, cultural background, current fitness and affective state all alter sensitivity to musical features; report and, where possible, control or stratify by these factors to interpret group and within‑subject effects.


## Measuring physiological reactions

There are numerous physiological measures that can be measured. Here we will look at some of the more popular ones. 

### Skin conductance

Skin conductance (also called electrodermal activity, EDA) is a simple way to see sympathetic arousal: when people get surprised, excited, or stressed, sweat‑gland activity changes and the skin conducts electricity differently. In recordings we separate a slow baseline level (skin conductance level, SCL) from quick event‑linked peaks (skin conductance responses, SCRs). In music studies you typically expect SCR peaks after surprising or high‑arousal moments, and SCL shifts when arousal stays up for longer.

Record EDA from stable sites such as the palms or soles, where the signal is strongest. Use good skin contact, clean the skin, and sample at least 10–50 Hz (higher if you need very precise timing). Try to keep the participant still and the electrodes steady, because movement and poor contact make the signal noisy.

Before analysis remove slow drifts and separate tonic and phasic parts of the signal (this can be done with simple filtering or with deconvolution methods). Find SCRs using clear amplitude and timing rules and always visually inspect the data to remove obvious motion artifacts. SCRs to brief musical events usually appear with a latency around 1–4 seconds after the event.

When reporting results use event‑related windows (report latency, amplitude, and how often responses occur). Normalize measures across participants (for example z‑scores or percent change) so differences in baseline skin conductance do not dominate. Also record and report likely confounds — room temperature and humidity, skin hydration, electrode placement, movement, and relevant medications — and correct statistically for multiple trials or comparisons where needed.

### Heart activity 
Electrocardiography (ECG) is the standard way to measure the heart: electrodes on the chest pick up the electrical signal of each heartbeat and give very precise R‑peak timing. From those R–R intervals you can compute instantaneous heart rate and fine beat‑to‑beat dynamics. Wearable optical sensors (photoplethysmography, PPG) on the wrist, finger or ear can track heart rate comfortably and well at rest, but they are more sensitive to motion and less reliable for short‑term HRV or spectral analyses. Choose ECG when you need millisecond timing (common sampling: 250–1000 Hz); PPG is OK for simple heart‑rate tracking (common sampling: 50–200 Hz).

To get useful measures you must clean the heartbeat series. Use a robust QRS/beat detector, remove or correct ectopic beats and clear artifacts (by rules and visual inspection), and interpolate short gaps so HR and HRV are not distorted. If you use PPG, check that beats align with ECG where possible and reject epochs with motion artifacts. Report the sensor type, placement and sampling rate so others can judge data quality.

Report each participant’s baseline heart rate and use within‑subject normalization (percent change, z‑scores, or baseline subtraction) because resting HR and reactivity vary with age, fitness, medication and posture. For experiments, typical analyses look at event‑locked heart‑rate windows (e.g., peak/trough magnitude and latency after a musical cue), and time‑resolved HRV to follow slow changes across a piece.

Heart‑rate variability (HRV) gives complementary information about autonomic balance. Simple time‑domain measures like RMSSD and SDNN are easy to compute; RMSSD (and high‑frequency power in the frequency domain) mainly reflect vagal (parasympathetic) influence and breathing‑linked modulation (respiratory sinus arrhythmia). Low‑frequency power and LF/HF ratios are harder to interpret and need caution. Always record respiration or a respiratory proxy to separate true vagal effects from breathing‑driven rhythms.

For music studies, prefer event‑locked and time‑resolved analyses rather than only long averages, and consider joint models that include respiration and movement (EMG or accelerometry) so you can tell apart autonomic from metabolic or motor effects. Finally, report effect sizes and uncertainty (confidence intervals or bootstrapped estimates) and describe preprocessing steps clearly so results are reproducible.

### Respiration

Respiration is the record of how people breathe—how fast, how deep, and when they inhale and exhale. In experiments we usually measure it with a breathing belt (respiratory inductance plethysmography, RIP), a nasal cannula, capnography, or impedance pneumography. Belts are comfortable and good for phase and timing; nasal or capnography are more precise for airflow but can feel intrusive. Whatever you use, make sure the respiration signal is synchronized with heart (ECG/PPG), skin conductance (EDA/GSR) and the musical stimulus markers so you can compare them exactly in time.

The main respiration variables to look at are breathing rate (how many breaths per minute), tidal depth (how big each breath is), the timing of inhalation versus exhalation, and instantaneous breathing phase (where in the breath cycle you are at any moment). For belt signals a sampling rate of about 25–50 Hz is usually enough to resolve when inhalations and exhalations begin and end. Always report sensor type, placement, and sampling rate so others can reproduce your work.

Music changes breathing in intuitive ways: slow, calm music and long phrases tend to slow breathing and make breaths deeper, while fast or strongly accented music tends to speed breathing and shift when people inhale. These changes can be subtle and depend on attention, task (listening vs. singing/dancing), and individual differences, so include control or baseline recordings when possible.

Respiration matters not only on its own but because it affects the heart. Breathing rhythms produce respiratory sinus arrhythmia (RSA), a regular heart‑rate fluctuation linked to inhalation/exhalation, so cardiac measures (HR, HRV) can look different depending on breathing. To avoid misinterpreting heart effects as purely autonomic, always record respiration alongside ECG/PPG, analyze respiration phase and depth relative to musical onsets, and consider joint analyses or simple mediation checks to see whether breathing explains heart‑rate changes or true autonomic shifts.

### Muscle tension

Electromyography (EMG) measures the tiny electrical signals that muscles make when they contract. In music research it is useful for separating motor activity (playing an instrument, singing, tapping, or expressive facial movements) from purely autonomic responses like heart rate or skin conductance. EMG can show when muscles activate and the relative strength and timing of those activations, which helps explain how movement and expression interact with musical perception or performance.

Typical EMG recordings use surface bipolar electrodes placed on the skin over the muscle of interest; sometimes fine (intramuscular) electrodes are used for deep or very specific muscles. Good skin preparation and a reference electrode reduce noise and improve signal quality. Record at a high sampling rate (commonly ≥1000 Hz) so the fast muscle signals are captured.

Raw EMG is noisy, so preprocessing is important: apply a band‑pass filter (for example ~20–450 Hz) to remove slow drift and high‑frequency noise, use a notch filter at mains frequency (50/60 Hz) if needed, then rectify (take the absolute value) and smooth (for example compute an RMS or low‑pass envelope) to produce an amplitude signal that is easier to interpret. Normalize EMG amplitudes to a task‑relevant maximum (MVC, maximum voluntary contraction) or to a baseline level so you can compare across participants and conditions.

Be aware of common problems: large movement artifacts, electrode slipping, and crosstalk from nearby muscles can contaminate the signal. Always report exact electrode sites, amplifier settings/gain, filter parameters, sampling rate, and the normalization method used so others can interpret and reproduce your results.

### Body temperature

Core temperature (measured rectally or tympanically) reflects true internal body heat. Most wearable sensors used in music studies measure skin (peripheral) temperature instead; skin temperature primarily indicates local blood flow near the sensor and is strongly influenced by the surrounding environment, so it does not reliably track very fast emotional reactions.

Skin temperature changes relatively slowly—over seconds to minutes—so you should expect gradual trends rather than sharp, moment‑to‑moment peaks in response to musical events. For most musicology applications a sampling rate of about 1 Hz (one sample per second) is sufficient to capture relevant variation.

Sensor placement matters: common sites are the fingertip, wrist, or chest, and you should always report exactly where you placed the sensor. Also record or control ambient factors that strongly affect skin temperature, such as room temperature, clothing, recent physical activity, and time of day (circadian effects).

For interpretation, combine skin temperature with other autonomic measures (for example ECG and EDA) so you can distinguish vasomotor/blood‑flow changes from other autonomic activity. When reporting results, always state sensor type, placement, sampling rate, and the ambient conditions so others can interpret slow temperature changes in your music experiments.

### Comparison

Here is a comparison of the above mentioned signals, what they capture and their strengths and limitations. 

| Signal | What it indexes | Typical sensors / form | Recommended sampling (Hz) | Notes (strengths / limitations) |
|---|---:|---|---:|---|
| ECG / PPG | Cardiac timing, heart rate, HRV | ECG chest electrodes or adhesive leads; PPG wrist/finger/ear optical | ECG: 250–1000; PPG: 50–200 | ECG = gold standard for precise R‑peaks & HRV; PPG easier/wearable but motion‑sensitive and less accurate for short‑term HRV |
| GSR / EDA | Sympathetic arousal, sweat‑gland activity (SCL, SCR) | Ag/AgCl electrodes on palmar/plantar sites | 10–50 (higher for fine phasic timing) | Direct index of sympathetic activity; slow tonic changes and phasic SCRs; sensitive to temperature, humidity, contact quality and movement |
| Respiration | Breathing rate, depth, phase (RSA) | RIP belts, nasal cannula, capnography, impedance | 25–100 | Essential to separate RSA from HRV; belt signals robust but can slip; nasal sensors more precise but intrusive |
| Skin temperature | Peripheral vasoconstriction/vasodilation, thermoregulation | Thermistors, thermocouples, infrared sensors (skin sites) | 1–10 | Reflects slow vasomotor changes; strongly affected by ambient conditions and clothing; useful for longer trends, not phasic responses |
| EMG | Muscle activation, tension, facial expressions, vocal‑tract activity | Surface bipolar electrodes (or intramuscular for depth) | ≥1000 (typical) | High temporal resolution to dissociate motor from autonomic effects; requires careful placement, normalization, and artifact control (crosstalk, movement) |

Typical study uses: cardiac (ECG/PPG) for HR/HRV and entrainment; EDA for arousal/phasic SCRs; respiration to disambiguate RSA and assess breathing entrainment; skin temp for slow autonomic/vasomotor trends; EMG to control motor confounds and capture expressive gestures; EEG for cortical correlates of perception/attention.

## Conclusion

ECG / PPG (heart rate, HRV): Records heartbeats and beat‑to‑beat variability and is used to index arousal and to test whether listeners’ heart rhythms entrain to music or performers; practical notes—ECG gives precise R‑peaks and is preferred for HRV, PPG is more wearable but motion‑sensitive, and heart signals are strongly affected by respiration and movement so always record respiration concurrently and minimize motion.

EDA / GSR (skin conductance): Measures tiny changes in skin conductance from sweat‑gland activity and is useful because phasic peaks mark sudden arousal or surprise while tonic level indexes sustained arousal; practical notes—signals show slow baseline drift, are sensitive to room temperature and electrode contact, and require stable placement and preprocessing to separate tonic and phasic components.

Respiration: Tracks breathing rate, depth and phase and is essential for determining whether heart‑rate changes arise from respiratory sinus arrhythmia or from other autonomic processes and for assessing entrainment to tempo or phrasing; practical notes—use belt or nasal sensors that resolve phase, record at sufficient sampling rate, and always synchronize respiration with ECG/EDA to disambiguate effects.

Skin temperature: Measures peripheral skin temperature that reflects slow vasomotor changes (stress vs. relaxation) over minutes rather than phasic responses; practical notes—changes are gradual and strongly influenced by ambient temperature, clothing and local blood flow, so report sensor site and room conditions and use temperature mainly for longer‑term trends alongside other autonomic measures.

EMG (muscle activity): Records skeletal muscle activation (face, jaw, limbs) and is useful for detecting expressive gestures and separating motor artifacts from autonomic signals; practical notes—movement creates large artifacts, electrodes require careful placement and normalization (e.g., MVC), and high sampling rates and filtering are needed to control crosstalk and noise.

Keep analyses simple and reproducible: always report what you measured, exact sensor placement, sampling rates, baseline procedures and any movement or physiological controls so musical effects can be interpreted reliably.

## Questions

1. How does musical tempo and rhythmic regularity affect heart rate and HRV, and how would you design an experiment to test cardiac entrainment while controlling for respiration and movement?
2. Which EDA measures (tonic SCL vs. phasic SCRs) best capture arousal and surprise in music, and what preprocessing and detection criteria ensure reliable SCR identification?
3. What analytic approaches can separate respiration‑driven RSA from vagal modulation in HRV when music alters breathing rate and depth?
4. How can EMG and accelerometry be combined to dissociate motor activity (singing, tapping, dancing) from autonomic changes in ECG/EDA recordings during live or interactive music tasks?
5. For field or concert studies, what sensor types, placements, and sampling rates are recommended for concurrent ECG/PPG, EDA, respiration and skin temperature, and how should motion, ambient temperature, and contact quality confounds be handled?