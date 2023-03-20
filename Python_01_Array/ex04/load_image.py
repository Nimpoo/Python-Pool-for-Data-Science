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
        img_gray = Image.open(path).convert('L')
    except FileNotFoundError as e:
        print(e)
        return (None)

    np_image = np.array(img)
    np_image_gray = np.array(img_gray)

    try:
        x1, x2, y1, y2 = 100, 500, 450, 850

        np_image_gray = np_image_gray[x1:x2, y1:y2]

        np_image_gray = np_image_gray.transpose()

    except TypeError as e:
        print(e)
        return (None)

    print(f"The shape of image is: {np_image_gray.shape}")
    print(np_image)

    img.close()
    img_gray.close()

    return (np_image_gray)