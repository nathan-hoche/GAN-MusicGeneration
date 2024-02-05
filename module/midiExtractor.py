from music21 import corpus, converter, instrument, note, stream, chord, duration
# from midi2audio import FluidSynth
# from midiutil.MidiFile import MIDIFile

NoteEncodedCase = {}
NoteDecodeCase = {}
DurationEncodedCase = {}
DurationDecodeCase = {}

class midiExtractor():
    def __init__(self, filename) -> None:
        self.filename = filename
        self.music = converter.parse(filename)
        self.chords = self.music.chordify()
        self.notes, self.durations = [], []

    def extract(self) :
        notes = []
        durations = []

        for element in self.chords.flatten():    
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

    def encodeNotes(self):
        encodedNote = []
        for note in self.notes:
            if note not in NoteEncodedCase:
                NoteEncodedCase[note] = len(NoteEncodedCase)
                NoteDecodeCase[len(NoteEncodedCase)-1] = note
            encodedNote.append(NoteEncodedCase[note])
        self.notes = encodedNote
        return self.notes
    
    def encodeDuration(self):
        encodedDuration = []
        for duration in self.durations:
            if duration not in DurationEncodedCase:
                DurationEncodedCase[duration] = len(DurationEncodedCase)
                DurationDecodeCase[len(DurationEncodedCase)-1] = duration
            encodedDuration.append(DurationEncodedCase[duration])
        self.durations = encodedDuration
        return self.durations
    
    def decodeNotes(self):
        decodedNote = []
        for note in self.notes:
            decodedNote.append(NoteDecodeCase[note])
        self.notes = decodedNote
        return self.notes
    
    def decodeDuration(self):
        decodedDuration = []
        for duration in self.durations:
            decodedDuration.append(DurationDecodeCase[duration])
        self.durations = decodedDuration
        return self.durations

if __name__ == "__main__":
    midiExtractor = midiExtractor("../select-midi/1238.midi")
    notes, durations = midiExtractor.extract()
    midiExtractor.displayData()
    print(midiExtractor.encodeNotes())
    print(midiExtractor.encodeDuration())