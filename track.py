from midiFile import MidiFile

class Track:

    #Constantes
    CHANNEL = 0
    DURATION = 0
    BPM = 60

    def __init__(self, numberTracks, time = 0):
        self.track = 0
        self.octave = 0
        self.instrument = 25
        self._volume = 100
        self.time = time
        self.mf = MidiFile(numberTracks, self.track, self.BPM, self.time)
        self.changeInstrument(self.instrument)


    def newTrack(self, tempo=BPM):
        self.track += 1
        self.tempo = tempo

        self.mf.addTrack(self.track, self.time, self.tempo)

    def addNote(self, pitch, duration=1, channel=CHANNEL, track=None, pause=0):
        if track is None:
            track = self.track

        self.mf.addNote(track, channel, pitch, self.time, duration, self._volume)
        self.time += 1+pause
    
    def changeInstrument(self, instrument, track=None, time=None):
        if track is None:
            track = self.track
        if time is None:
            time = self.time

        self.mf.changeInstrument(track, self.CHANNEL, time, instrument)

    def finishMusic(self, musicName):
        self.mf.save(musicName)
