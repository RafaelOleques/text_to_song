class Translator:
  TRANSLATION_TABLE = {
    'C': 60,
    'D': 62,
    'E': 64,
    'F': 65,
    'G': 67,
    'A': 69,
    'B': 71,
    'a': 'REPEAT_NOTE',
    'b': 'REPEAT_NOTE',
    'c': 'REPEAT_NOTE',
    'd': 'REPEAT_NOTE',
    'e': 'REPEAT_NOTE',
    'f': 'REPEAT_NOTE',
    ' ': 'VOLUME_DOUBLE',
    '!': 'CHANGE_INSTRUMENT_114',
    'I': 'CHANGE_INSTRUMENT_7',
    'O': 'CHANGE_INSTRUMENT_7',
    'U': 'CHANGE_INSTRUMENT_7',
    'i': 'CHANGE_INSTRUMENT_7',
    'o': 'CHANGE_INSTRUMENT_7',
    'u': 'CHANGE_INSTRUMENT_7',
    '1': 'CHANGE_INSTRUMENT_PLUS_1',
    '2': 'CHANGE_INSTRUMENT_PLUS_2',
    '3': 'CHANGE_INSTRUMENT_PLUS_3',
    '4': 'CHANGE_INSTRUMENT_PLUS_4',
    '5': 'CHANGE_INSTRUMENT_PLUS_5',
    '6': 'CHANGE_INSTRUMENT_PLUS_6',
    '7': 'CHANGE_INSTRUMENT_PLUS_7',
    '8': 'CHANGE_INSTRUMENT_PLUS_8',
    '9': 'CHANGE_INSTRUMENT_PLUS_9',
    '?': 'OCTAVE_UP',
    '.': 'OCTAVE_UP',
    '\n': 'CHANGE_INSTRUMENT_15',
    ';': 'CHANGE_INSTRUMENT_76',
    ',': 'CHANGE_INSTRUMENT_20',
    '-': 'VOLUME_DEFAULT',
    '+': 'VOLUME_DOUBLE',
    'b+': 'BPM_PLUS_50',
    'b-': 'BPM_MINUS_50',
    'o+': 'OCTAVE_UP',
    'o-': 'OCTAVE_DOWN',
  }

  # EX entrada: 'A-Db+?b\nk'
  # EX saida: ['A', 'VOLUME_DEFAULT', 'D', 'BPM_PLUS_50', 'OCTAVE_UP', 'REPEAT_NOTE', 'CHANGE_INSTRUMENT_15', 'REPEAT_NOTE']

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
        instructions_seq.append( 'REPEAT_NOTE' )
    return instructions_seq

if __name__ == "__main__":
  trad = Translator()
  texto = "a-Db+?b\nkqs9we-d -e9hf9ifwbefoqri0e"
  print('entrada:', texto)
  print('saida:', trad.translate_text_to_instructions(texto))
