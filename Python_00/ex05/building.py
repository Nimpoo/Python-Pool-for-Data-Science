import sys


def nbr_upper_letters(str):

    '''Count the number of upper letter in str'''

    res = 0
    for c in str:
        if c.isupper():
            res += 1

    return (res)


def nbr_lower_letters(str):

    '''Count the number of lower letter in str'''

    res = 0
    for c in str:
        if c.islower():
            res += 1

    return (res)


def nbr_spaces(str):

    '''Count the number of space in str'''

    res = 0
    for c in str:
        if c.isspace():
            res += 1

    return (res)


def nbr_ponctuations(str):

    '''Count the number of ponctuation in str'''

    res = 0
    for c in str:
        if c in ("!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"):
            res += 1

    return (res)


def nbr_digits(str):

    '''Count the number of digit in str'''

    res = 0
    for c in str:
        if c.isdigit():
            res += 1

    return (res)


if __name__ == '__main__':

    str = ""

    assertionError = "AssertionError: more than one argument are provided"

    try:
        assert len(sys.argv) <= 2, assertionError
    except AssertionError as e:
        print(e)
        sys.exit()

    if len(sys.argv) == 1:
        print("What is the text to count?")
        for line in sys.stdin:
            str += line
            break

    elif len(sys.argv) == 2:
        str = sys.argv[1]

    total = nbr_upper_letters(str) + nbr_lower_letters(str)
    total += nbr_ponctuations(str) + nbr_spaces(str) + nbr_digits(str)

    print("The text contains", total, "characters:")

    print(nbr_upper_letters(str), "upper letters")
    print(nbr_lower_letters(str), "lower letters")
    print(nbr_ponctuations(str), "ponctuation marks")
    print(nbr_spaces(str), "spaces")
    print(nbr_digits(str), "digits")
