'''Biblioteca que transforma texto para música'''
from pyknon.genmidi import Midi
from pyknon.music import NoteSeq

'''Biblioteca para pegar o tempo'''
from datetime import datetime

'''Gera o nome do arquivo'''
now = datetime.now()
archive_dir = "./musicas/"
archive_name = str(now.strftime("%d%m%Y%H%M%S"))
archive_extension = ".midi"

'''Realiza a conversao'''
notes1 = NoteSeq("D4 F#8 A Bb4")
midi = Midi(1, tempo=90)
midi.seq_notes(notes1, track=0)
midi.write(archive_dir+archive_name+archive_extension)