from midiFile import MidiFile

class Track:

    #Default
    CHANNEL = 0
    DURATION = 0
    BPM = 60

    def __init__(self, numberTracks, time = 0):
        self.track = 0
        self.time = 0
        self.octave = 0
        self.instrument = 25
        self.time = time
        self.mf = MidiFile(numberTracks, self.track, self.BPM, self.time)
        self.changeInstrument(self.instrument)


    def newTrack(self, trackName="", tempo=BPM):
        self.track =+ 1
        self.tempo = tempo

        self.mf.addTrack(self.track, self.time, self.tempo)
        
        if(trackName == ""):
            self.trackName = str(self.track)
        else:
            self.trackName = trackName

    def addNote(self, pitch, volume, duration=1, channel=CHANNEL, track=None, pause=0):
        if track is None:
            track = self.track

        self.mf.addNote(track, channel, pitch, self.time, duration, volume)
        self.time += 1+pause
    
    def changeInstrument(self, instrument, track=None, time=None):
        if track is None:
            track = self.track
        if time is None:
            time = self.time

        self.mf.changeInstrument(track, self.CHANNEL, time, instrument)

    def finishMusic(self, musicName):
        self.mf.save(musicName)
