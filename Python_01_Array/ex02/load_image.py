import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:

    '''Load and display a triple array of each
    pixel of an image'''

    error_type = "TypeError: pls enter a str type"
    error_permi = "PermissionError: permission denied"

    try:
        if not isinstance(path, str):
            raise TypeError

        if not path.endswith(".jpeg") and not path.endswith(".jpg"):
            raise TypeError

        img = Image.open(path)

    except FileNotFoundError as e:
        print(e)
        return (None)
    except TypeError:
        print(error_type)
        return (None)
    except AttributeError as e:
        print(e)
        return (None)
    except PermissionError:
        print(error_permi)
        return (None)

    np_image = np.array(img)

    print(f"The shape of image is: {np_image.shape}")

    return (np_image)
