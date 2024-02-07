
# GANSynth

## Technique used

| Type | Name |
| --- | --- |
| Model | Progressive GAN + Convolution |
| DATASET | NSynth |
| Type of Generation | Instantaneous Frequency (IF) |
| Type of Data | Audio |

## Observation make

1. Difficult to generate coherent wavefroms, the alignment of the waveforms is difficult to achieve :

![WaveForm](https://magenta.tensorflow.org/assets/gansynth/waves_with_frames.png)

2. GANs which genere Instantaneous Frequency (IF) for the phase component outperform other representations + More coherent than waveforms$

![Comparison](https://magenta.tensorflow.org/assets/gansynth/coherence.png)

3. Progressive training (P) and increasing the frequency resolution of the STFT (H) boosts performance by helping to separate closely-spaced harmonics

![Comparison](https://magenta.tensorflow.org/assets/gansynth/comparison.png)

> Papers: [Papers](https://magenta.tensorflow.org/gansynth)

# JukeBox

## Technique used

| Type | Name |
| --- | --- |
| Model | VQ-VAE-2 |
| DATASET | LyricWiki  |
| Type of Generation | Spectrogram |
| Type of Data | Audio |

# Modification of the VQ-VAE-2

1. Use spectrogram as input
2. Use spectral loss to train the model
3. Separate each decoders to maximize the use of the upper levels (the moste encoded ones)
4. Randomly reset a codebook vector to one of the encoded hidden states -> whenever its usage falls below a threshold.

## Observation make

1. VQ-VAE have a hiearchy colapse problem -> solved by the VQ-VAE-2

![VQ-VAE](https://production-media.paperswithcode.com/methods/Screen_Shot_2020-06-28_at_4.26.40_PM.png)

![Spectrogram Convert](https://www.researchgate.net/publication/350892531/figure/fig1/AS:1013059212554241@1618543546246/Proposed-VQ-VAE-2-architecture-for-spectrograms-The-encoder-converts-1024-128-large.png)


> Papers: [Papers](https://openai.com/research/jukebox)

# MuseGAN

## Technique used

| Type | Name |
| --- | --- |
| Model | GANs |
| DATASET | Lakh MIDI |
| Type of Generation | Piano Rolls of instruments (bass, drums, guitar, strings, piano) |
| Type of Data | Rock MIDI |

## Approach

1. 3 models proposed:
    - Jamming model (Each instrument is generated independently -> multiple discriminator for each instrument)
    - Composer model (Each instrument is generated at the same time -> one single discriminator)
    - Hybrid model (Each instrument is generated independently -> one single discriminator)

## Observation make

1. Need a temporal model to generate music
2. Each instrument in the same song has a different temporal dynamics -> but all interdependant
4. No clear way to identify which track plays the melody and which one plays the harmony or other accompaniment
4. The Hybrid model is preferred in general

> Papers: [Papers](https://salu133445.github.io/musegan/pdf/musegan-aaai2018-paper.pdf)

# MuseNet

## Technique used

| Type | Name |
| --- | --- |
| Model | Transformer |
| DATASET | Classical Archive, BitMidi, MAESTRO |
| Type of Generation | Given a set of notes (Piano rolls???), predict the following notes |
| Type of Data | Midi |

> Not a lot of information about this model

> Papers: [Papers](https://openai.com/research/musenet)

# Music Transformer

## Technique used

| Type | Name |
| --- | --- |
| Model | Attention based Neural Network |
| DATASET | JSB Chorales and Piano-e-Competition |
| Type of Generation | Symbolic representation |
| Type of Data | Midi |

> Papers: [Papers](https://arxiv.org/abs/1809.04281)

# MidiNet

## Technique used

| Type | Name |
| --- | --- |
| Model | GANS (Convolution for the generator) |
| DATASET | TheoryTab |
| Type of Generation | Symbolic representation |
| Type of Data | Pops Midi |


> Papers: [Papers](https://arxiv.org/abs/1703.10847)

# C-RNN-GAN

> Papers: [Papers](https://arxiv.org/pdf/1611.09904.pdf)

# WaveNet

> Papers: [Papers](https://arxiv.org/pdf/1609.03499v2.pdf)

# WaveGAN

> Papers: [Papers](https://arxiv.org/pdf/1802.04208v3.pdf)