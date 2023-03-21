import numpy as np

from PIL import Image


def ft_load(path: str) -> np.array:

    '''Load, rotate to 90 degrees and display a triple array of each
    pixel of an image, slice it, then return a gray equivalent
    copy of his numpy array'''

    error_type = "TypeError: pls enter a str type"

    try:
        if not isinstance(path, str):
            raise TypeError

        img = Image.open(path)

    except FileNotFoundError as e:
        print(e)
        exit()
    except TypeError:
        print(error_type)
        exit()
    except AttributeError as e:
        print(e)
        exit()

    np_image = np.array(img)

    print(f"The shape of image is: {np_image.shape}")
    print(np_image)

    img.close()

    return (np_image)
