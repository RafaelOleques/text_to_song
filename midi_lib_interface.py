from midiutil.MidiFile import MIDIFile

# Encapsula funções de interface com a biblioteca base de geração de arquivos MIDI.
# A biblioteca usada é a midiutil
class Midi_lib_interface:
    def __init__(self, numberTracks, track, bpm, time):
        self.mf = MIDIFile(numberTracks)
        self.mf.addTrackName(track, time, str(track))
        self.mf.addTempo(track, time, bpm)

    # Adiciona uma trilha de som
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
