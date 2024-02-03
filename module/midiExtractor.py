import mido
from music21 import corpus, converter, instrument, note, stream, chord, duration
# from midi2audio import FluidSynth
# from midiutil.MidiFile import MIDIFile

import matplotlib.pyplot as plt

NB_NOTES_PER_GROUP = 100


class midiExtractor():
    def __init__(self, filename) -> None:
        self.filename = filename
        self.music = converter.parse(filename)
        self.chords = self.music.chordify()

    def displayChords(self):
        self.chords.show()


if __name__ == "__main__":
    midiExtractor = midiExtractor("../maestro-v3.0.0-midi/2004/MIDI-Unprocessed_SMF_02_R1_2004_01-05_ORIG_MID--AUDIO_02_R1_2004_05_Track05_wav.midi")
    midiExtractor.displayChords()