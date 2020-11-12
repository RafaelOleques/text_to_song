from midiutil.MidiFile import MIDIFile

class MidiFile:
    def __init__(self, numberTracks, track, bpm, time):
        self.mf = MIDIFile(numberTracks)
        self.mf.addTrackName(track, time, str(track))
        self.mf.addTempo(track, time, bpm)

    def addTrack(self, track, time, tempo):
        self.mf.addTempo(track, time, tempo)
        self.mf.addTrackName(track, time, str(track))

    def addNote(self, track, channel, pitch, time, duration, volume):
        self.mf.addNote(track, channel, pitch, time, duration, volume)

    def addTempo(self, track, time, bpm):
        self.mf.addTempo(track, time, bpm)

    def changeInstrument(self, track, channel, time, instrument):
        self.mf.addProgramChange(track, channel, time, instrument)

    def save(self, musicName):
        with open("./musicas/"+musicName+".mid", 'wb') as outf:
            self.mf.writeFile(outf)
