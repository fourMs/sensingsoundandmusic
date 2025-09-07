# Week 6: Frequency and Timbre

Frequency is a fundamental concept in music and sound, referring to the number of vibrations or cycles per second of a sound wave, measured in Hertz (Hz). It is the basis for understanding pitch, tone, and other auditory phenomena.

## Auditory Stream Segregation



### Pitch
[Pitch](https://en.wikipedia.org/wiki/Pitch_(music)) is the perceptual property of sounds that allows their ordering on a frequency-related scale. It is closely tied to the fundamental frequency (F0) of a sound wave. The unit of measurement for pitch is Hertz (Hz), which represents the number of cycles per second. 

- **F0 (Fundamental Frequency):** The lowest frequency of a sound wave, which determines the perceived pitch.
- **Hertz (Hz):** The unit of frequency measurement.
- **Tone:** A sound with a specific pitch and timbre.
- **Note:** A musical symbol representing a specific pitch and duration.
- **Missing Fundamental:** A phenomenon where the brain perceives the pitch of a sound even when its fundamental frequency is absent.

### Harmony
[Harmony](https://en.wikipedia.org/wiki/Harmony) involves the combination of discernible tones to create intervals and chords. It is the simultaneous sounding of different pitches, which can evoke a wide range of emotional responses.

- **Discernible Tones:** Individual pitches that can be identified and combined.
- **Intervals:** The difference in pitch between two tones.
- **Chords:** A group of notes played together to create a harmonic structure.

Harmony plays a crucial role in the emotional tone and complexity of music. Tools like chord recognition software and harmonic analysis enable the study and creation of harmonic structures.

### Timbre
[Timbre](https://en.wikipedia.org/wiki/Timbre), often called "sound color," is the quality of a sound that distinguishes different instruments or voices, even when they produce the same pitch and loudness.

- **"Sound Color":** The unique quality that makes a violin sound different from a flute.
- **Temporal Alignment:** The timing of sound waves that contributes to timbre perception.
- **Just Noticeable Differences (JND):** The smallest change in a sound property that can be perceived.

Technological tools like spectral analysis and synthesizers are used to analyze and recreate timbre, enabling sound design and instrument modeling.

### Texture
[Texture](https://en.wikipedia.org/wiki/Texture_(music)) describes how multiple layers of sound interact in a musical composition. It ranges from monophonic (a single melody) to polyphonic (multiple independent melodies).

- **Combination of Timbres:** The blending of different sound qualities to create a rich texture.

In music production, digital audio workstations (DAWs) and multitrack recording allow for the manipulation and layering of textures.

### Analysis-by-Synthesis
[Analysis-by-Synthesis](https://en.wikipedia.org/wiki/Analysis_by_synthesis) is a method used in sound and music research to understand auditory perception by recreating sounds and analyzing their properties. This approach is widely used in areas like speech synthesis, sound design, and music analysis.

### Melody
[Melody](https://en.wikipedia.org/wiki/Melody) is the sequence of musical notes that are perceived as a single entity. It is often the most recognizable and memorable aspect of a musical piece. Melody plays a crucial role in emotional engagement and memory recall. Tools like MIDI editors and pitch detection algorithms are used to analyze and manipulate melodies.

### Rhythm
[Rhythm](https://en.wikipedia.org/wiki/Rhythm) refers to the pattern of sounds and silences in time. It is a fundamental aspect of music that organizes the flow of notes and beats. Rhythm contributes to the energy and movement of a piece, influencing how listeners perceive and engage with music.



### Audio Visualizations

- **Waveform**: A visual representation of amplitude over time. [Learn more](https://en.wikipedia.org/wiki/Waveform)
- **Spectrogram**: Displays frequency content over time. [Learn more](https://en.wikipedia.org/wiki/Spectrogram)
- **Log Mel Spectrogram**: Mimics human hearing by applying the Short-Time Fourier Transform (STFT), Mel band-pass filters, and a logarithmic transformation to represent audio on a decibel scale. Widely used in audio-related tasks for its perceptual relevance. [Learn more](https://en.wikipedia.org/wiki/Mel-frequency_cepstrum)
- **MFCCs (Mel-Frequency Cepstral Coefficients)**: Extracts and compresses audio features by applying the Discrete Cosine Transform (DCT) to the Log Mel spectrum. Commonly used in speech processing, music classification, and music information retrieval. [Learn more](https://en.wikipedia.org/wiki/Mel-frequency_cepstrum)
- **CQT (Constant-Q Transform)**: Uses a logarithmic frequency scale with exponentially spaced center frequencies and varying filter bandwidths. Ideal for musical note frequency extraction and analysis. [Learn more](https://en.wikipedia.org/wiki/Constant-Q_transform)


import numpy as np
import librosa

import matplotlib.pyplot as plt
import librosa.display

# Generate a test audio signal (sine wave + harmonics)
sr = 22050  # sample rate
duration = 2.0  # seconds
t = np.linspace(0, duration, int(sr * duration), endpoint=False)
f_start = 0
f_end = 20000
audio = 0.5 * np.sin(2 * np.pi * ((f_start + (f_end - f_start) * t / duration) * t))

fig, axs = plt.subplots(3, 2, figsize=(14, 12))
fig.suptitle('Audio Representations', fontsize=16)

# Waveform
librosa.display.waveshow(audio, sr=sr, ax=axs[0, 0])
axs[0, 0].set_title('Waveform')
axs[0, 0].set_xlabel('')
axs[0, 0].set_ylabel('Amplitude')

# Spectrogram
S = np.abs(librosa.stft(audio, n_fft=1024, hop_length=256))
librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max), sr=sr, hop_length=256, x_axis='time', y_axis='hz', ax=axs[0, 1])
axs[0, 1].set_title('Spectrogram (dB)')

# Mel Spectrogram
S_mel = librosa.feature.melspectrogram(y=audio, sr=sr, n_fft=1024, hop_length=256, n_mels=64)
librosa.display.specshow(librosa.power_to_db(S_mel, ref=np.max), sr=sr, hop_length=256, x_axis='time', y_axis='mel', ax=axs[1, 0])
axs[1, 0].set_title('Mel Spectrogram (dB)')

# MFCC
mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13, n_fft=1024, hop_length=256)
librosa.display.specshow(mfccs, x_axis='time', ax=axs[1, 1])
axs[1, 1].set_title('MFCC')

# CQT
C = np.abs(librosa.cqt(audio, sr=sr, hop_length=256, n_bins=60))
librosa.display.specshow(librosa.amplitude_to_db(C, ref=np.max), sr=sr, hop_length=256, x_axis='time', y_axis='cqt_note', ax=axs[2, 0])
axs[2, 0].set_title('CQT (dB)')

# Hide the last empty subplot
axs[2, 1].axis('off')

plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.show()

### Symbolic Representations

#### MIDI
MIDI (Musical Instrument Digital Interface) is a standard protocol for communicating musical performance data between electronic instruments and computers. It encodes information such as note pitch, velocity, duration, and control changes. [Learn more](https://en.wikipedia.org/wiki/MIDI)

#### ABC Notation
ABC Notation is a text-based music notation system that uses ASCII characters to represent musical scores. It is widely used for folk and traditional music due to its simplicity and compatibility with text-based tools. [Learn more](https://en.wikipedia.org/wiki/ABC_notation)

#### REMI
REMI (REvamped MIDI-derived events) is an enhanced representation of MIDI data designed to better capture musical rhythm and structure. It introduces features like Note Duration events, Bar and Position tokens, and Tempo events, making it suitable for music generation tasks. [Learn more](https://arxiv.org/abs/2002.00212)

#### MusicXML
MusicXML is an XML-based format for representing Western music notation. It encodes detailed musical elements such as notes, rests, articulations, and dynamics, making it ideal for sharing and analyzing sheet music. [Learn more](https://en.wikipedia.org/wiki/MusicXML)

#### Piano Roll
The Piano Roll is a visual representation of music, where time is displayed on the horizontal axis and pitch on the vertical axis. Notes are represented as rectangles, with their length indicating duration. It is commonly used in digital audio workstations (DAWs) for music editing and analysis. [Learn more](https://en.wikipedia.org/wiki/Piano_roll)

#### Note Graph
A Note Graph is a graph-based representation of musical scores, where nodes represent notes and edges capture relationships such as sequence, onset, and sustain. This approach provides a structured way to analyze and model complex musical relationships. [Learn more](https://arxiv.org/abs/2006.05417)



import music21
music21.environment.UserSettings()['musescoreDirectPNGPath'] = '/usr/bin/mscore3'

# Create a simple melody: C D E F G F E D C
melody_notes = ['C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4', 'D4', 'C4']
melody = music21.stream.Stream()
for n in melody_notes:
    melody.append(music21.note.Note(n, quarterLength=0.5))

# Show the musical score (this will render in Jupyter if MuseScore or similar is installed)
melody.show()

## Citations

the following syntax: `` {cite}`holdgraf_evidence_2014` `` 

Here is the bibliography


```{bibliography}
```
