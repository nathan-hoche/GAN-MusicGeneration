from music21 import corpus, converter, instrument, note, stream, chord, duration
# from midi2audio import FluidSynth
# from midiutil.MidiFile import MIDIFile

class midiExtractor():
    def __init__(self, filename) -> None:
        self.filename = filename
        self.music = converter.parse(filename)
        self.chords = self.music.chordify()
        self.notes, self.durations = [], []

    def extract(self) :
        notes = []
        durations = []

        for element in self.chords.flat:    
            if isinstance(element, chord.Chord):
                notes.append('.'.join(n.nameWithOctave for n in element.pitches))
                durations.append(element.duration.quarterLength)

            if isinstance(element, note.Note):
                if element.isRest:
                    notes.append(str(element.name))
                    durations.append(element.duration.quarterLength)
                else:
                    notes.append(str(element.nameWithOctave))
                    durations.append(element.duration.quarterLength) 
        self.notes = notes
        self.durations = durations  
        return notes, durations
    
    def displayData(self):
        print("| Duration | Note |")
        print("|----------|------|")
        for note, duration in zip(self.notes, self.durations):
            print("|", duration, "\t|", note, "\t|")

if __name__ == "__main__":
    midiExtractor = midiExtractor("../select-midi/1238.midi")
    notes, durations = midiExtractor.extract()
    midiExtractor.displayData()