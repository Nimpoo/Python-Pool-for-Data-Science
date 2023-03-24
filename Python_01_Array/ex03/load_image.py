import numpy as np

from PIL import Image


def ft_load(path: str) -> np.array:

    '''Load and display a triple array of each
    pixel of an image, and return a gray equivalent
    copy of his numpy array'''

    error_type = "TypeError: pls enter a str type"
    error_permi = "PermissionError: permission denied"

    try:
        if not isinstance(path, str):
            raise TypeError

        if not path.endswith(".jpeg") and not path.endswith(".jpg"):
            raise TypeError

        img = Image.open(path)
        img_gray = Image.open(path).convert("L")

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
    np_image_gray = np.array(img_gray)

    print(f"The shape of image is: {np_image.shape}")
    print(np_image)

    img.close()
    img_gray.close()

    return (np_image_gray)
