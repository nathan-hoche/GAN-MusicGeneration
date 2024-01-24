import torch
import torchaudio
import torchaudio.functional as F
import torchaudio.transforms as T

import librosa
import matplotlib.pyplot as plt

torch.random.manual_seed(0)

class audioExtractor():
    def __init__(self) -> None:
        self.spectrogram = T.Spectrogram(n_fft=512)

    def load_audio(self, file):
        waveform, sample_rate = torchaudio.load(file)
        return waveform, sample_rate

    def getSpectrogram(self, waveform):
        return self.spectrogram(waveform)
                    
    
    def plot_waveform(self, waveform, sample_rate, title="Waveform", ax=None):
        waveform = waveform.numpy()

        num_channels, num_frames = waveform.shape
        time_axis = torch.arange(0, num_frames) / sample_rate

        if ax is None:
            _, ax = plt.subplots(num_channels, 1)
        ax.plot(time_axis, waveform[0], linewidth=1)
        ax.grid(True)
        ax.set_xlim([0, time_axis[-1]])
        ax.set_title(title)
    
    def plot_specgram(self, specgram, title=None, ylabel="freq_bin", ax=None):
        if ax is None:
            _, ax = plt.subplots(1, 1)
        if title is not None:
            ax.set_title(title)
        ax.set_ylabel(ylabel)
        ax.imshow(librosa.power_to_db(specgram), origin="lower", aspect="auto", interpolation="nearest")


if __name__ == "__main__":
    extractor = audioExtractor()
    waveform, sample_rate = extractor.load_audio("data/1-100032-A-0.wav")
    specgram = extractor.getSpectrogram(waveform)
    fig, axs = plt.subplots(2, 1)
    extractor.plot_waveform(waveform, sample_rate)
    extractor.plot_specgram(specgram[0], title="Spectrogram", ylabel="Hz")
    fig.tight_layout()
    plt.show()