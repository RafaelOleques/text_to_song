from translator import Translator
from track import Track

class Generator:

  def __init__(self, text, musicName, initialBPM, initialInstrument):
    self._text = text
    self._instructions = Translator().translate_text_to_instructions(self._text)
    print('Array de instrucoes:', self._instructions)
    self._track = Track(1)
    self._musicName = musicName
    self._initial_bpm = initialBPM
    self._initialInstrument = initialInstrument

  def generate_song(self):
    for instruction in self._instructions:
      method = instruction[0]
      arg = instruction[1]
      callTrackMethod = getattr(self._track, method, 'repeatNote')
      print(callTrackMethod)
      callTrackMethod(arg)
    self._track.finishMusic(self._musicName)

if __name__ == "__main__":
  texto = "CDE9FGABD"
  generator = Generator(texto, 'Testando_generator', 120, 100)
  generator.generate_song()
