import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:

    '''Give the BMI of the between list height and weight'''

    error_type = "TypeError: pls enter a int/float type"
    error_type_list = "TypeError: pls enter a list"

    if not isinstance(height, list) or not isinstance(weight, list):
        print(error_type_list)
        return (list([]))

    for elem in height:
        if not isinstance(elem, int) and not isinstance(elem, float):
            print(error_type)
            return (list([]))

    for elem in weight:
        if not isinstance(elem, int) and not isinstance(elem, float):
            print(error_type)
            return (list([]))

    np_height = np.array(height)
    np_weight = np.array(weight)

    bmi = np_weight/np_height**2
    return (bmi.tolist())


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:

    '''Append True in list if BMI < limit, else return False and return it'''

    lst_bool = []

    if bmi is None:
        print("TypeError: pls enter a int/float type")
        return (lst_bool)

    for elem in bmi:
        if not isinstance(elem, int) and not isinstance(elem, float):
            print("TypeError: pls enter a int/float type")
            return (lst_bool)

    for elem in bmi:
        if elem < float(limit):
            lst_bool.append(True)
        else:
            lst_bool.append(False)

    return (lst_bool)
