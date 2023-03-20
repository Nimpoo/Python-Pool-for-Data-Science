import numpy as np


def slice_me(family: list, start: int, end: int) -> list:

    '''Oh no !!! 😱 This function slice my whole family ! 😣
return the familit to start from end, return empty
list if it's not valid'''

    error_type = "TypeError: pls enter a int/float type"
    error_type_list = "TypeError: pls enter a list"

    if not isinstance(family, list):
        print(error_type_list)
        return (list([]))

    for elem in family:
        if not isinstance(elem, list):
            print(error_type_list)
            return (list([]))

    if not isinstance(start, int) and not isinstance(start, float):
        print(error_type)
        return (list([]))

    if not isinstance(end, int) and not isinstance(end, float):
        print(error_type)
        return (list([]))

    np_family = np.array(family)
    print(f"My shape is : {np_family.shape}")

    np_family_sliced = np_family[start:end:,]
    print(f"My new shape is : {np_family_sliced.shape}")

    return (np_family_sliced.tolist())
