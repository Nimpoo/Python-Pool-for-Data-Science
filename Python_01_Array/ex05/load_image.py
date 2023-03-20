import numpy as np

from PIL import Image


def ft_load(path: str) -> np.array:

    '''Load, rotate to 90 degrees and display a triple array of each
    pixel of an image, slice it, then return a gray equivalent
    copy of his numpy array'''

    error_type = "TypeError: pls enter a str type"

    if not isinstance(path, str):
        print(error_type)
        return (None)

    try:
        img = Image.open(path)
    except FileNotFoundError as e:
        print(e)
        return (None)

    np_image = np.array(img)

    print(f"The shape of image is: {np_image.shape}")
    print(np_image)

    img.close()

    return (np_image)
