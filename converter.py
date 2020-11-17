import subprocess

# Classe para converter MIDI para .wav
class Converter:

  def convert_midi_to_audio(self, midi_file, soundfonts_file, out_dir):
    out_file = out_dir + '/converted_audio.wav'
    subprocess.call(['fluidsynth', '-T', 'wav', '-F', out_file, '-ni', soundfonts_file, midi_file])
