# Gan-MusicGeneration

## Introduction

The objective of this Epitech Hub's Project is to generate music using a Generative Adversarial Network (GAN) or an Auto Encoder (AE). The GAN/AE are mainly used to generate images, but I wanted to explore the interest of using them to generate music. The project will be done in Python using Keras.

## Task to complete

| Task | Time Estimated | Definition of Done | Status |
| ---- | -------------- |  ------------------ | ------ |
| Research on the subject | 2 days | [x] Find 10 interesting papers on how to generate music <br> [-] Resume for all of them which technique <br> [x] Find 5 interesting datasets for our case <br> [-] Describe the content of the dataset and list the type music that can be generated with each dataset | ❌ |
| Prepare the dataset | 2 days |  [-] Format the dataset in order to be used in the training process of the desired GAN <br> [x] Handle error case in the dataset (iex: if MIDI, handle empty tracks) <br> [x] Handle error case in the dataset (if music not encoded in the same way) | ❌ |
| Implement a GAN or a AE | 2 days |  [x] Research on how to implement the choosen GAN (put sources) <br> [x] Implement the GAN in a simple case (such as MINST) <br> [x] Train the GAN in order that it is able to generate image | ✅ |
| Convert the GAN to handle music file | 2 days | [-] Research on how to use music data in a GAN <br> [-] Implement the GAN on the dataset <br> [-] Train the GAN in order that it is able to generate music | ❌ |
|-|-|-|-|
| TOTAL| 8 days | 7/13 DODs | ❌ | 

## How to use the project

### Requirements

- Python 3.11
- FluidSynth
- Juptyer Notebook

> Other requirements are listed in the `requirements.txt` file

### Installation

```bash
git clone git@github.com:nathan-hoche/GAN-MusicGeneration.git
```

### Usage

In order to launch the training process, you have multiple steps to follow:
1. Download the [Maestro Dataset](https://magenta.tensorflow.org/datasets/maestro) (In MIDI format)
2. Launch AudioConverter.py to convert the MIDI files (from a specific composer) to WAV files
3. Launch the training process

```bash
python3 main.py
```

## Project Details

### Dataset

The dataset used for this project is the [Maestro Dataset](https://magenta.tensorflow.org/datasets/maestro). The reason why I choose this dataset is because I wanted to generate a music in the style of a specific composer. This project can be easily adapted to generate music in another style by using the same dataset. It is also possible to use another dataset, but it will require to adapt the code.

[0] Curtis Hawthorne, Andriy Stasyuk, Adam Roberts, Ian Simon, Cheng-Zhi Anna Huang, Sander Dieleman, Erich Elsen, Jesse Engel, and Douglas Eck. "Enabling Factorized Piano Music Modeling and Generation with the MAESTRO Dataset." In International Conference on Learning Representations, 2019.

### Preprocessing

In order to use the audio files in the GAN, I first try to use spectrogram. But I quickly realized that it was not the best way to do it. I tried to make a spectrogram from a sample of the dataset and reverse the process using torchAudio, but I got this result:

![Spectrogram](data/images/Spectrogram.png)

As you can see, the reconstruction is not good enough to be used in a GAN.


### Model

First, In order to learn how to create a GAN, I decided to make a GAN which would be able to generate mnist images. I want to specially thanks the authors of [this repository](https://github.com/eriklindernoren/Keras-GAN), which was a big help in my understansing on how to implement GAN.

[1] I. J. Goodfellow et al., “Generative Adversarial Networks,” arXiv.org, 2014. https://arxiv.org/abs/1406.2661
‌




## Interesting Papers

| Name | Link | Year | Technique | Note |
| ---- | ---- | ---- | --------- | ---- |
| GANSynth | [Github](https://github.com/magenta/magenta/tree/main/magenta/models/gansynth) / [Papers](https://magenta.tensorflow.org/gansynth) | 2019 | ProgressiveGAN, AudioFile |  |
| JukeBox | [Github](https://github.com/openai/jukebox/) / [Papers](https://openai.com/research/jukebox) | 2020 | VQ-VAE, AudioFile |  |
| MuseGAN | [Github](https://github.com/salu133445/musegan) / [Papers](https://salu133445.github.io/musegan) | 2018 | GAN, MIDI |  |
| MuseNet | [Papers](https://openai.com/research/musenet) | 2019 | GPT-2, MIDI |  |
| MidiNet | [Github](https://github.com/RichardYang40148/MidiNet/tree/master/v1) / [Papers](https://arxiv.org/abs/1703.10847) | 2017 | GAN, MIDI |  |
| IncoGAN | [Papers](https://www.mdpi.com/2227-7390/9/4/387) | 2021 | GAN, AudioFile |  |
| C-RNN-GAN | [Papers](https://arxiv.org/pdf/1611.09904.pdf) | 2016 | GAN, MIDI |  |
| Quantized GAN | [Papers](https://arxiv.org/pdf/2204.00604.pdf) | 2022 | GAN, AudioFile |  |
| WaveNet | [Papers](https://arxiv.org/pdf/1609.03499v2.pdf) | 2016 |  AudioFile |  |
| WaveGAN | [Papers](https://arxiv.org/pdf/1802.04208v3.pdf) | 2019 | GAN, AudioFile |  |

## Interesting Dataset

| Name | Link | DataType | Type of Music | Number of Music | Note |
| ---- | ---- | -------- | ------------- | --------------- | ---- |
| BitMidi | [link](https://bitmidi.com) | MIDI | ALL | 113,000+ |  |
| Classical Archives | [link](https://www.classicalarchives.com/newca/#!/) | MIDI/Music | Classical | 20,000+ Midi / 934,000 audio file |  |
| MAESTRO | [link](https://magenta.tensorflow.org/datasets/maestro) | MIDI/Audio | Pianist | 200 hours of performance | |
| Classical Music Midi | [link](https://www.kaggle.com/datasets/soumikrakshit/classical-music-midi/data?select=bach) | MIDI | Classical | 295 Midi |  |
| GTZAN Dataset - Music Genre Classification | [link](https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification/data) | Audio | All | 1000 audio file |  |