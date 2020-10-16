from midiutil.MidiFile import MIDIFile

class Track:

    #Default
    CHANNEL = 0
    DURATION = 0
    BPM = 60
    track = 0
    time = 0
    octave = 0
    instrument = 25

    def __init__(self, numberTracks, _time = time):
        self.mf = MIDIFile(numberTracks)
        self.time = _time
        self.mf.addTrackName(self.track, self.time, str(self.track))
        self.mf.addTempo(self.track, self.time, self.BPM)
        self.changeInstrument(self.instrument)


    def newTrack(self, trackName="", tempo=BPM):
        self.track =+ 1
        self.tempo = tempo

        self.mf.addTempo(self.track, self.time, tempo)
        self.mf.addTrackName(self.track, self.time, str(self.track))
        
        if(trackName == ""):
            self.trackName = str(self.track)
        else:
            self.trackName = trackName

    def addNote(self, pitch, volume, duration=1, channel=CHANNEL, _track=None, pause=0):
        if _track is None:
            _track = self.track

        self.mf.addNote(_track, channel, pitch, self.time, duration, volume)
        self.time += 1+pause
    
    def changeInstrument(self, _instrument, _track=None, _time=None):
        if _track is None:
            _track = self.track
        if _time is None:
            _time = self.time

        self.mf.addProgramChange(_track, self.CHANNEL, _time, _instrument)

    def finishMusic(self, musicName):
        with open("./musicas/"+musicName+".mid", 'wb') as outf:
            self.mf.writeFile(outf)
