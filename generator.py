from translator import Translator
from track import Track

class Generator:

    def __init__(self, text, musicName):
        self.text = text
        self.track = Track(1)
        self.musicName = musicName

    def generate_song(self):
        self.track.addNote(60, 100)
        self.track.addNote(64, 100)
        self.track.addNote(67, 100)
        self.track.changeInstrument(81)
        self.track.addNote(60, 100)
        self.track.addNote(64, 100)
        self.track.addNote(67, 100)

        self.track.finishMusic(self.musicName)
