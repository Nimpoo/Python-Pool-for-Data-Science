from numpy import array
from PIL import Image

import numpy as np


def ft_invert(array) -> array:

    '''Take the numpy array of an image in parameter.
    The function invert the color and return this converted array'''

    np_invert = np.copy(array)

    np_invert[:, :, 0] = 255 - np_invert[:, :, 0]
    np_invert[:, :, 1] = 255 - np_invert[:, :, 1]
    np_invert[:, :, 2] = 255 - np_invert[:, :, 2]

    np_invert_img = Image.fromarray(np_invert)
    np_invert_img.show()

    return (np_invert)


def ft_red(array) -> array:

    '''Take the numpy array of an image in parameter.
    The function convert the whole color in red and return his array'''

    np_red = np.copy(array)

    np_red[:, :, 1] = 0
    np_red[:, :, 2] = 0

    np_red_img = Image.fromarray(np_red)
    np_red_img.show()

    return (np_red)


def ft_green(array) -> array:

    '''Take the numpy array of an image in parameter.
    The function convert the whole color in green and return his array'''

    np_green = np.copy(array)

    np_green[:, :, 0] = 0
    np_green[:, :, 2] = 0

    np_green_img = Image.fromarray(np_green)
    np_green_img.show()

    return (np_green)


def ft_blue(array) -> array:

    '''Take the numpy array of an image in parameter.
    The function convert the whole color in blue and return his array'''

    np_blue = np.copy(array)

    np_blue[:, :, 0] = 0
    np_blue[:, :, 1] = 0

    np_blue_img = Image.fromarray(np_blue)
    np_blue_img.show()

    return (np_blue)


def ft_grey(array) -> array:

    '''Take the numpy array of an image in parameter.
    The function convert the whole color in grey and return his array'''

    np_grey = np.copy(array)

    np_grey = np.mean(np_grey, axis=2)

    np_grey_img = Image.fromarray(np_grey)
    np_grey_img.show()

    return (np_grey)
