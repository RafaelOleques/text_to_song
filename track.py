from midi_lib_interface import Midi_lib_interface as MidiFile

class Track:

  # Constantes padrão de classe
  CHANNEL = 0
  DURATION = 0
  VOLUME = 60
  OCTAVE = 5
  BPM = None
  INSTRUMENT = None
  
  def __init__(self, numberTracks, initialBPM, initialInstrument, time = 0):
    # Setamos o instrumento e BPM iniciais nas constantes de classe dos mesmos
    self.INSTRUMENT = initialInstrument
    self.BPM = initialBPM

    self._track = 0
    self._octave = self.OCTAVE
    self._instrument = self.INSTRUMENT
    self._volume = self.VOLUME
    self._time = time
    self._bpm = self.BPM
    # Criação do objeto MidiFile o qual adicionaremos as notas e editaremos os parâmetros da música
    self._lib_interface = MidiFile(numberTracks, self.getTrack(), self.getBpm(), self.getTime())
    # Booleano que indica se o último método chamado foi o AddNote()
    self._last_method_is_addnote = False
    # Variável que salva a última nota tocada
    self._last_pitch = None
    
    # Setamos o instrumento inicial do MidiFile
    self.setInstrument(self.getInstrument())

  def getTrack(self):
    return self._track

  def setTrack(self, track):
    self._track = track
  
  def getOctave(self):
    return self._octave

  def setOctave(self, octave):
    # A biblioteca MidiUtil não aceita oitavas fora do intervalo 0..9
    MIN_OCTAVE = 0
    MAX_OCTAVE = 9

    if octave < MIN_OCTAVE:
      self._octave = MIN_OCTAVE
    elif octave > MAX_OCTAVE:
      self._octave = self.OCTAVE
    else:
      self._octave = octave

  def getInstrument(self):
    return self._instrument

  def setInstrument(self, instrument, track = None, time = None):
     # A biblioteca MidiUtil aceita valores de instrumento entre 0 e 255,
     # mas eles repetem a partir do 127. Sendo assim, limitamos o intervalo.
    MIN_INSTRUMENT = 0
    MAX_INSTRUMENT = 127
    self.setLastMethodIsAddnote(False)

    if track is None:
      track = self.getTrack()
    if time is None:
      time = self.getTime()

    if instrument < MIN_INSTRUMENT:
      self._instrument = MIN_INSTRUMENT
    elif instrument > MAX_INSTRUMENT:
      self._instrument = self.INSTRUMENT
    else:
      self._instrument = instrument

    self._lib_interface.changeInstrument(track, self.CHANNEL, time, self.getInstrument())

  def getVolume(self):
    return self._volume

  def setVolume(self, volume):
     # A biblioteca MidiUtil não aceita volumes fora do intervalo 0..127
    MIN_VOLUME = 0
    MAX_VOLUME = 127
    if volume < MIN_VOLUME:
      self._volume = MIN_VOLUME
    elif volume > MAX_VOLUME:
      self._volume = self.VOLUME
    else:
      self._volume = volume

  def getTime(self):
    return self._time

  def setTime(self, time):
    self._time = time

  def getBpm(self):
    return self._bpm

  def setBpm(self, bpm):
     # A biblioteca MidiUtil não aceita um BPM menor do que 4
    MIN_BPM = 4
    if bpm < MIN_BPM:
      self._bpm = MIN_BPM
    else:
      self._bpm = bpm

  def getLastMethodIsAddnote(self):
    return self._last_method_is_addnote

  def setLastMethodIsAddnote(self, boolean):
    self._last_method_is_addnote = boolean

  def getLastPitch(self):
    return self._last_pitch

  def setLastPitch(self, last_pitch):
    self._last_pitch = last_pitch

  def addNote(self, pitch, duration=1, channel=CHANNEL, time = None, track=None, pause=0, volume = None):
    OCTAVE_SIZE = 12
    self.setLastMethodIsAddnote(True)

    if track is None:
      track = self.getTrack()
    if volume is None:
      volume = self.getVolume()
    if time is None:
      time = self.getTime()

    # Calcula a nota na oitava pedida
    pitch_in_octave = pitch + self.getOctave() * OCTAVE_SIZE

    self._lib_interface.addNote(track, channel, pitch_in_octave, time, duration, volume)
    self.setLastPitch(pitch)
    # Avança uma posição na linha do tempo do MidiFile
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

    self._lib_interface.addTempo(self.getTrack(), self.getTime(), self.getBpm())

  def finishMusic(self, musicName):
    self._lib_interface.save(musicName)
