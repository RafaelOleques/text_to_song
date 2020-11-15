import subprocess

class Converter:

  def convert_midi_to_audio(self, midi_file, soundfonts_file, out_dir):
    out_file = out_dir + '/converted_audio.wav'
    subprocess.call(['fluidsynth', '-T', 'wav', '-F', out_file, '-ni', soundfonts_file, midi_file])

if __name__ == "__main__":
  converter = Converter()
  converter.convert_midi_to_audio('musicas/Testando_generator.mid', '/usr/share/sounds/sf2/FluidR3_GM.sf2', '.')
