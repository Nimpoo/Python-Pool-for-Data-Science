from load_image import ft_load

import matplotlib.pyplot as plt


if __name__ == '__main__':

    try:
        np_image_gray = ft_load("animal.jpeg")

        x1, x2, y1, y2 = 100, 500, 450, 850

        np_image_gray = np_image_gray[x1:x2, y1:y2]

    except TypeError as e:
        print(e)
        exit()

    # plt.axis([x1, x2, y1, y2])
    # plt.axis('off')

    print(f"New shape after slicing: {np_image_gray.shape}")
    print(np_image_gray)

    plt.imshow(np_image_gray, cmap='gray')
    plt.show()
