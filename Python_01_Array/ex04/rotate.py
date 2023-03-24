from load_image import ft_load

import matplotlib.pyplot as plt


if __name__ == '__main__':

    try:
        np_image_gray_90 = ft_load("animal.jpeg")

    except TypeError as e:
        print(e)
        exit()

    print(f"New shape after Transpose: {np_image_gray_90.shape}")
    print(np_image_gray_90)

    plt.imshow(np_image_gray_90, cmap='gray')
    plt.show()
