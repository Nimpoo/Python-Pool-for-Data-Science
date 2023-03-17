def count_in_list(lst: list, occurence: str) -> int:
    '''Count the number of occurence and return it'''

    res = 0
    for elem in lst:
        if elem is occurence:
            res += 1

    return res
