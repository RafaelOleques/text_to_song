class Translator:
    
    notes = {
        'A': 9,
        'B': 11,
        'C': 0,
        'D': 2,
        'E': 4,
        'F': 5,
        'G': 7
    }

    operations = {
        '+': 'VOLUME_DOUBLE',
        '-': 'VOLUME_DEFAULT',

        'O+': 'OCTAVE_UP',
        'O-': 'OCTAVE_DOWN',

        'I': 'REPEAT_NOTE',
        'O': 'REPEAT_NOTE',
        'U': 'REPEAT_NOTE',

        '?': 'RANDOM_NOTE',
        '.': 'RANDOM_NOTE',

        ' ': 'PAUSE',

        'B+': 'BPM_PLUS_50',
        'B-': 'BPM_MINUS_50',

        '\n': 'CHANGE_INSTRUMENT'
    }
