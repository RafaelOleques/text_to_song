from midiFile import MidiFile

class Track:

  #Constantes
  CHANNEL = 0
  DURATION = 0
  BPM = 60
  VOLUME = 30
  OCTAVE = 5
  INSTRUMENT = 25

  def __init__(self, numberTracks, time = 0):
    self.__track = 0
    self.__octave = self.OCTAVE
    self.__instrument = self.INSTRUMENT
    self.__volume = self.VOLUME
    self.__time = time
    self.__mf = MidiFile(numberTracks, self.getTrack(), self.BPM, self.getTime())
    self.__bpm = self.BPM
    self.__last_method_is_addnote = False
    self.__last_pitch = None
    
    self.setInstrument(self.getInstrument())

  def getTrack(self):
    return self.__track

  def setTrack(self, track):
    self.__track = track
  
  def getOctave(self):
    return self.__octave

  def setOctave(self, octave):
    if octave < 0:
      self.__octave = 0
    elif octave > 9:
      self.__octave = self.OCTAVE
    else:
      self.__octave = octave

  def getInstrument(self):
    return self.__instrument

  def setInstrument(self, instrument, track = None, time = None):
    self.setLastMethodIsAddnote(False)
    if track is None:
      track = self.getTrack()
    if time is None:
      time = self.getTime()

    if instrument < 0:
      self.__instrument = 0
    elif instrument > 127:
      self.__instrument = self.INSTRUMENT
    else:
      self.__instrument = instrument

    self.__mf.changeInstrument(track, self.CHANNEL, time, self.getInstrument())

  def getVolume(self):
    return self.__volume

  def setVolume(self, volume):
    if volume < 0:
      self.__volume = 0
    elif volume > 127:
      self.__volume = self.VOLUME
    else:
      self.__volume = volume

  def getTime(self):
    return self.__time

  def setTime(self, time):
    self.__time = time

  def getBpm(self):
    return self.__bpm

  def setBpm(self, bpm):
    if bpm < 4:
      self.__bpm = 4
    else:
      self.__bpm = bpm

  def getLastMethodIsAddnote(self):
    return self.__last_method_is_addnote

  def setLastMethodIsAddnote(self, boolean):
    self.__last_method_is_addnote = boolean

  def getLastPitch(self):
    return self.__last_pitch

  def setLastPitch(self, last_pitch):
    self.__last_pitch = last_pitch

  def newTrack(self, tempo=BPM):
    self.track += 1
    self.tempo = tempo

    self.mf.addTrack(self.track, self.time, self.tempo)

  def addNote(self, pitch, duration=1, channel=CHANNEL, time = None, track=None, pause=0, volume = None):
    self.setLastMethodIsAddnote(True)
    if track is None:
      track = self.getTrack()
    if volume is None:
      volume = self.getVolume()
    if time is None:
      time = self.getTime()

    pitch_in_octave = pitch + self.getOctave() * 12

    self.__mf.addNote(track, channel, pitch_in_octave, time, duration, volume)
    self.setLastPitch(pitch)
    self.setTime(self.getTime() + 1 + pause)

  def addPause(self):
    self.addNote(self.getLastPitch(), volume = 0)

  def repeatNote(self, bool):
    if self.getLastMethodIsAddnote() == True:
      self.addNote(self.getLastPitch())
    else:
      self.addPause()
    self.setLastMethodIsAddnote(False)

  def multiplyVolume(self, multiplier):
    self.setLastMethodIsAddnote(False)
    self.setVolume(self.getVolume() * multiplier)

  def volumeDefault(self, boolean):
    self.setVolume(self.VOLUME)

  def changeInstrument(self, instrument):
    self.setLastMethodIsAddnote(False)
    self.setInstrument(self.getInstrument() + instrument)

  def changeOctave(self, diff):
    self.setLastMethodIsAddnote(False)
    self.setOctave(self.getOctave() + diff)

  def changeBPM(self, diff):
    self.setLastMethodIsAddnote(False)
    self.setBpm(self.getBpm() + diff)

    self.__mf.addTempo(self.getTrack(), self.getTime(), self.getBpm())

  def finishMusic(self, musicName):
    self.__mf.save(musicName)
