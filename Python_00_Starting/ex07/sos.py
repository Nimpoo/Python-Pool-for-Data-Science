import sys


if __name__ == '__main__':

    arg = sys.argv
    len_arg = len(arg[1])

    assertionError = "AssertionError: the arguments are bad"

    morse_code = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....',
    'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----',
    '2': '..---', '3': '...--',
    '4': '....-', '5': '.....',
    '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    ' ': '/'
    }

    try:

        if ( len(arg) != 2 ):
            raise AssertionError(assertionError)
        for x in arg[1]:
            if ( not x.isalnum() or not x.isspace() ):
                raise AssertionError(assertionError)
            # print(" ".join(morse_code[x.upper()] for x in arg[1]))

        for x in arg[1]:
            print(morse_code[x.upper()], end = "")
        if (len_arg > 1):
            print(' ', end = "")
            len_arg -= 1
        print()

    except AssertionError as e:
        print(e)
