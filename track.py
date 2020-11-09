from midiFile import MidiFile

class Track:

  #Constantes
  CHANNEL = 0
  DURATION = 0
  BPM = 60
  VOLUME = 30

  def __init__(self, numberTracks, time = 0):
    self.track = 1
    self.octave = 5
    self.instrument = 25
    self._volume = self.VOLUME
    self.time = time
    self.mf = MidiFile(numberTracks, self.track, self.BPM, self.time)
    self.bpm = self.BPM
    self.last_pitch = 0
    self.setInstrument(self.instrument)


  def newTrack(self, tempo=BPM):
    self.track += 1
    self.tempo = tempo

    self.mf.addTrack(self.track, self.time, self.tempo)

  def addNote(self, pitch, duration=1, channel=CHANNEL, track=None, pause=0):
    if track is None:
      track = self.track
    
    pitch_in_octave = pitch + self.octave * 12

    self.mf.addNote(track, channel, pitch_in_octave, self.time, duration, self._volume)
    self.last_pitch = pitch
    self.time += 1+pause

  def repeatNote(self, bool):
    self.addNote(self.last_pitch)

  def multiplyVolume(self, multiplier):
    if (self._volume * 2) < 127:
      self._volume *= 2
    else:
      self._volume = self.VOLUME

  def setInstrument(self, instrument, track = None, time = None):
    if track is None:
      track = self.track
    if time is None:
      time = self.time

    self.mf.changeInstrument(track, self.CHANNEL, time, instrument)
  
  def changeInstrument(self, instrument):
    new_instrument = self.instrument + instrument
    self.setInstrument(new_instrument)

  def changeOctave(self, diff):
    self.octave = self.octave + diff

  # does not work yet
  # def changeBPM(self, diff):
  #   new_tempo = self.bpm + diff
  #   self.newTrack()


  def finishMusic(self, musicName):
    self.mf.save(musicName)
