import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:

    '''Give the BMI of the between list height and weight'''

    error_type = "TypeError: bad type input"
    error_divide_zero = "ZeroDivisionError: pls use real number"
    error_len_list = "ValueError: use 2 list with the same lengh plz"

    try:
        if not isinstance(height, list) or not isinstance(weight, list):
            raise TypeError

        if len(height) != len(weight):
            raise ValueError

        for elem in height:
            if elem <= 0:
                raise ZeroDivisionError
            if not isinstance(elem, int) and not isinstance(elem, float):
                raise TypeError(error_type)

        for elem in weight:
            if elem <= 0:
                raise ZeroDivisionError
            if not isinstance(elem, int) and not isinstance(elem, float):
                raise TypeError(error_type)

    except ZeroDivisionError:
        print(error_divide_zero)
        exit()
    except TypeError:
        print(error_type)
        exit()
    except ValueError:
        print(error_len_list)
        exit()

    np_height = np.array(height)
    np_weight = np.array(weight)

    return list(np_weight/np_height**2)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:

    '''Append True in list if BMI < limit, else return False and return it'''

    error_type = "TypeError: bad type input"

    lst_bool = []

    try:
        if bmi is None:
            raise TypeError

        for elem in bmi:
            if not isinstance(elem, int) and not isinstance(elem, float):
                raise TypeError

    except TypeError:
        print(error_type)
        exit()

    for elem in bmi:
        if elem < float(limit):
            lst_bool.append(False)
        else:
            lst_bool.append(True)

    return (lst_bool)
