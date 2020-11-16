class Input_information_converter:

  #Recebe uma tupla no formato (type, input) em que:
  # - type é o que está sendo recebido: file ou text
  # - input é o caminho de um arquivo ou uma string qualquer

  def __init__(self, information):
    TYPE  = 0
    INPUT = 1

    self._type  = information[TYPE]
    self._input = information[INPUT]

  def _extract_file_information(self):
    text = open(self._input, 'r', encoding='utf-8-sig')
    converted_text = ""

    for line in text:
      converted_text += line

    return converted_text


  def get_text(self):
    if self._type == 'file':
      return self._extract_file_information()

    return self._input