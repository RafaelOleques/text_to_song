import subprocess

# Requisitos: sintetizador FluidSynth instalado no sistema; arquivo de samples de instrumento SoundFonts2
# 
# Converte um arquivo MIDI em arquivo de áudio usando uma fonte de samples de instrumento SoundFonts2
# e um sintetizador - utilizamos o FluidSynth.
# Invoca o sintetizador dentro de uma chamada de subprocesso pois não há uma versão em formato de lib Python.

class Converter:

  # Entrada: arquivo .mid
  # Saída: arquivo de áudio .wav
  def convert_midi_to_audio(self, midi_file, soundfonts_file, out_dir):
    out_file = out_dir + '/converted_audio.wav'
    subprocess.call(['fluidsynth', '-T', 'wav', '-F', out_file, '-ni', soundfonts_file, midi_file])
