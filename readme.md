# Gan-MusicGeneration

## Introduction

The objective of this Epitech Hub's Project is to generate music using a Generative Adversarial Network (GAN) or an Auto Encoder (AE). The GAN/AE are mainly used to generate images, but I wanted to explore the interest of using them to generate music. The project will be done in Python using Keras.

## Task to complete

| Task | Time Estimated | Definition of Done | Status |
| ---- | -------------- |  ------------------ | ------ |
| Research on the subject | 2 days | [ ] Find 10 interesting papers on how to generate music <br> [ ] Resume for all of them which technique <br> [ ] Find 5 interesting datasets for our case <br> [ ] Describe the content of the dataset and list the type music that can be generated with each dataset | ❌ |
| Prepare the dataset | 2 days |  [ ] Format the dataset in order to be used in the training process of the desired GAN <br> [ ] Handle error case in the dataset (iex: if MIDI, handle empty tracks) <br> [ ] Handle error case in the dataset (if music not encoded in the same way) | ❌ |
| Implement a GAN or a AE | 2 days |  [ ] Research on how to implement the choosen GAN (put sources) <br> [ ] Implement the GAN in a simple case (such as MINST) <br> [ ] Train the GAN in order that it is able to generate image | ❌ |
| Convert the GAN to handle music file | 2 days | [ ] Research on how to use music data in a GAN <br> [ ] Implement the GAN on the dataset <br> [ ] Train the GAN in order that it is able to generate music | ❌ |
|-|-|-|-|
| TOTAL| 8 days | 13 DODs | ❌ | 


## Interesting Papers

| Name | Link | Year | Technique | Note |
| ---- | ---- | ---- | --------- | ---- |
| GANSynth | [link](https://magenta.tensorflow.org/gansynth) | 2019 | ProgressiveGAN, AudioFile |  |
| JukeBox | [link](https://openai.com/research/jukebox) | 2020 | VQ-VAE, AudioFile |  |
| MuseGAN | [link](https://salu133445.github.io/musegan) | 2018 | GAN, MIDI |  |
| MuseNet | [link](https://openai.com/research/musenet) | 2019 | GPT-2, MIDI |  |
| MidiNet | [Github](https://github.com/RichardYang40148/MidiNet/tree/master/v1) / [Papers](https://arxiv.org/abs/1703.10847) | 2017 | GAN, MIDI |  |

## Interesting Dataset

| Name | Link | DataType | Type of Music | Number of Music | Note |
| ---- | ---- | -------- | ------------- | --------------- | ---- |
| BitMidi | [link](https://bitmidi.com) | MIDI | ALL | 113,000+ |  |
| Classical Archives | [link](https://www.classicalarchives.com/newca/#!/) | MIDI/Music | Classical | 20,000+ Midi / 934,000 audio file |  |
| MAESTRO | [link](https://magenta.tensorflow.org/datasets/maestro) | MIDI/Audio | Pianist | 200 hours of performance | |
