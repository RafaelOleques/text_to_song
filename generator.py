from translator import Translator
from track import Track
from input_information_converter import Input_information_converter

class Generator:

  def __init__(self, inputt, musicName, initialBPM, initialInstrument):
    input_converter = Input_information_converter(inputt)
    translator = Translator()

    self._text = input_converter.get_text()
    self._instructions = translator.translate_text_to_instructions(self._text)
    self._track = Track(1)
    self._musicName = musicName
    self._initial_bpm = initialBPM
    self._initialInstrument = initialInstrument

  def generate_song(self):
    METHOD = 0
    ARG = 1

    for instruction in self._instructions:
      method = instruction[METHOD]
      arg = instruction[ARG]
      callTrackMethod = getattr(self._track, method, 'repeatNote')
      callTrackMethod(arg)
    self._track.finishMusic(self._musicName)

if __name__ == "__main__":
  text = ('text', 'CDE9FGABD')
  generator = Generator(text, 'Testando_generator', 120, 100)
  generator.generate_song()
