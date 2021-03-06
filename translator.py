class Translator:
  TRANSLATION_TABLE = {
    'C': ('addNote', 0),
    'D': ('addNote', 2),
    'E': ('addNote', 4),
    'F': ('addNote', 5),
    'G': ('addNote', 7),
    'A': ('addNote', 9),
    'B': ('addNote', 11),
    'a': ('repeatNote', True),
    'b': ('repeatNote', True),
    'c': ('repeatNote', True),
    'd': ('repeatNote', True),
    'e': ('repeatNote', True),
    'f': ('repeatNote', True),
    ' ': ('multiplyVolume', 2),
    '!': ('setInstrument', 114),
    'I': ('setInstrument', 7),
    'O': ('setInstrument', 7),
    'U': ('setInstrument', 7),
    'i': ('setInstrument', 7),
    'o': ('setInstrument', 7),
    'u': ('setInstrument', 7),
    '1': ('changeInstrument', 1),
    '2': ('changeInstrument', 2),
    '3': ('changeInstrument', 3),
    '4': ('changeInstrument', 4),
    '5': ('changeInstrument', 5),
    '6': ('changeInstrument', 6),
    '7': ('changeInstrument', 7),
    '8': ('changeInstrument', 8),
    '9': ('changeInstrument', 9),
    '?': ('changeOctave', 1),
    '.': ('changeOctave', 1),
    '\n': ('setInstrument', 15),
    ';': ('setInstrument', 76),
    ',': ('setInstrument', 20),
    '-': ('volumeDefault', True),
    '+': ('multiplyVolume', 2),
    'b+': ('changeBPM', 50),
    'b-': ('changeBPM', -50),
    'o+': ('changeOctave', 1),
    'o-': ('changeOctave', -1),
  }

  # Recebe um texto não formatado como entrada e retorna um array de tuplas <instrução, argumento da instrução>.
  # EX entrada: 'CDE9F'
  # EX saida: [('addNote', 60), ('addNote', 62), ('addNote', 64), ('changeInstrument', 9), ('addNote', 65)]

  def translate_text_to_instructions(self, text):
    split_text = []
    split_text[:0] = text

    instructions_seq = []
    while (len(split_text) > 0):
      char = split_text.pop(0)
      if char in ['b', 'o']:
        if split_text[0] in ['+', '-']:
          char += split_text.pop(0)
      try:
        instructions_seq.append( self.TRANSLATION_TABLE[char] )
      except:
        instructions_seq.append( ('repeatNote', True) )
    return instructions_seq
