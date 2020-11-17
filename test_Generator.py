import os.path
from generator import Generator

class TestGenerator:    
    def test_generate_song_file(self):
        inputt = ("file", "teste.txt")
        musicName = "mymusic"
        initialBPM = 60
        initialInstrument = 120

        generate = Generator(inputt, musicName, initialBPM, initialInstrument)
        generate.generate_song()

        assert os.path.isfile("./musicas/"+musicName+".mid")
    
    def test_generate_song_string(self):
        inputt = ("text", "CDE9FGABD")
        musicName = "mymusic"
        initialBPM = 60
        initialInstrument = 120

        generate = Generator(inputt, musicName, initialBPM, initialInstrument)
        generate.generate_song()

        assert os.path.isfile("./musicas/"+musicName+".mid")
