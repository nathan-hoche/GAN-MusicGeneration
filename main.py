from module.audioExtractor import audioExtractor
import matplotlib.pyplot as plt

AudioExtractor = audioExtractor()

waveform, sampleRate = AudioExtractor.load_audio("convertedAudio/1251.wav")

Segments = AudioExtractor.segmentAudio(waveform, sampleRate)
SpecGram = AudioExtractor.getSpectrogram(Segments[3])

waveformReconstructed = AudioExtractor.getInverseSpectrogram(SpecGram)

fig, axs = plt.subplots(2, 1)
AudioExtractor.plot_waveform(Segments[3], sampleRate, ax=axs[0], title="Original")
AudioExtractor.plot_waveform(waveformReconstructed, sampleRate, ax=axs[1], title="Reconstructed")