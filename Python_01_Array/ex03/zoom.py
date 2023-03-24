from load_image import ft_load

import matplotlib.pyplot as plt


if __name__ == '__main__':

    try:
        np_image_gray = ft_load("animal.jpeg")

        x1, x2, y1, y2 = 450, 850, 100, 500

        np_image_gray = np_image_gray[y1:y2, x1:x2]

    except TypeError as e:
        print(e)
        exit()

    print(f"New shape after slicing: {np_image_gray.shape}")
    print(np_image_gray)

    plt.imshow(np_image_gray, cmap='gray')
    plt.show()
