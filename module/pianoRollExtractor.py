import pypianoroll
from midi2audio import FluidSynth
import os

class PianoRollExtractor:
    def __init__(self, path:str=None, pianoRoll:list=None):
        if path is None and pianoRoll is None:
            raise ValueError("path or pianoRoll should be given")
        self.path = path
        if path:
            self.pianoRoll = pypianoroll.read(self.path)
        elif pianoRoll.all() != None:
            track = pypianoroll.BinaryTrack(pianoroll=pianoRoll)
            self.pianoRoll = pypianoroll.Multitrack(tracks=[track])
        self.pianoRoll.binarize()

    def __str__(self) -> str:
        return self.path
    
    def trim(self, start:int, end:int) -> None:
        self.pianoRoll.trim(start, end * self.pianoRoll.resolution)
    
    # def getPartial(self, start:int, end:int) -> pypianoroll.Multitrack:
    #     track = pypianoroll.Track(self.pianoRoll.tracks[0].pianoroll)
    #     return pypianoroll.Multitrack(tracks=[track])

    def get_piano_roll(self, start:int=2, end:int=None) -> pypianoroll.Multitrack:
        if end is None:
            return self.pianoRoll.tracks[0].pianoroll[start * self.pianoRoll.resolution:]
        return self.pianoRoll.tracks[0].pianoroll[start * self.pianoRoll.resolution:end * self.pianoRoll.resolution]

    
    def plot(self) -> None:
        self.pianoRoll.plot()

    def save(self, path:str) -> None:
        self.pianoRoll.to_pretty_midi().write(path)
    
    def save_as_wav(self, path:str) -> None:
        self.pianoRoll.to_pretty_midi().write("output.mid")
        FluidSynth().midi_to_audio("output.mid", path)
        os.remove("output.mid")