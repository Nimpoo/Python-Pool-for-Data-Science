import sys





if __name__ == '__main__':

    print(filter.__doc__)






    numbers = [-2, -1, 0, 1, 2]

    nbr = list(filter(lambda n: n > 0, numbers))
    print(nbr)
