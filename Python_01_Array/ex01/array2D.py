import numpy as np


def slice_me(family: list, start: int, end: int) -> list:

    '''Oh no !!! 😱 This function slice my whole family ! 😣
return the familit to start from end, return empty
list if it's not valid'''

    error_type = "TypeError: bad type input"

    len_list = len(family[0])

    try:
        if not isinstance(family, list):
            raise TypeError

        for elem in family:
            if not isinstance(elem, list):
                raise TypeError
            if len(elem) != len_list:
                raise TypeError
            for elem2 in elem:
                if not isinstance(elem2, int) and not isinstance(elem2, float):
                    raise TypeError

        if not isinstance(start, int) and not isinstance(start, float):
            raise TypeError
        if type(elem) == bool:
            raise TypeError

        if not isinstance(end, int) and not isinstance(end, float):
            raise TypeError
        if type(elem) == bool:
            raise TypeError

    except TypeError:
        print(error_type)
        exit()

    np_family = np.array(family)
    print(f"My shape is : {np_family.shape}")

    np_family_sliced = np_family[start:end]
    print(f"My new shape is : {np_family_sliced.shape}")

    return (np_family_sliced.tolist())
