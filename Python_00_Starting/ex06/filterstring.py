import sys
from sys import argv

from ft_filter import ft_filter


if __name__ == '__main__':

    assertionError = "AssertionError: the arguments are bad"

    try:
        if (len(argv) != 3 or not argv[2].isdigit()):
            raise AssertionError(assertionError)
    except AssertionError as e:
        print(e)
        sys.exit()

    print(list(ft_filter(lambda x: len(x) > int(argv[2]), argv[1].split(' '))))
