import numpy as np
import cv2

from other_algo import algorithm_3, algorithm_4, algorithm_5


def two_d(image_b, gradient):
    # code for 2D Convolution
    image_c = image_b.copy()
    h, w = image_c.shape

    for i in range(1, h - 1):
        for j in range(1, w - 1):
            image_c[i, j] = np.sum(image_b[(i - 1):(i + 2), (j - 1):(j + 2)] * gradient)

    image_c = image_c / image_c.max()

    return image_c


def one_d(image_b, vertical, hori):
    # code for 1D Convolution
    img_b = cv2.copyMakeBorder(image_b, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=0)  # Adding border

    img_b = np.asarray(img_b, dtype=np.float32)  # img to array in float
    h, w = image_b.shape
    result = np.zeros((h, w))
    temp = np.zeros((h, w))

    for i in range(1, h - 1):
        for j in range(1, w - 1):
            temp[i][j] = np.sum(img_b[i, j - 1:j + 2] * hori)

    for i in range(1, h - 1):
        for j in range(1, w - 1):
            temp2 = np.array([[temp[i - 1][j]], [temp[i][j]], [temp[i + 1][j]]])
            result[i][j] = np.sum(temp2 * vertical)

    result = result / result.max()

    return result


def my_algorithm(img, algo_type):
    if algo_type == 2:
        print("algorithm_2 called")
        # Algorithm based on 2D Convolution
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        img_b = cv2.GaussianBlur(img, (3, 3), 0)  # reduce high frequency noise
        x = np.array((-1, 0, 1, -2, 0, 2, -1, 0, 1))
        y = np.array((-1, -2, -1, 0, 0, 0, 1, 2, 1))
        gx = np.reshape(x, [3, 3])  # gradient in x
        gy = np.reshape(y, [3, 3])  # gradient in y

        img_b = img_b.astype("float")

        ggx = two_d(img_b, gx)
        ggy = two_d(img_b, gy)

        g = np.sqrt(ggx * ggx + ggy * ggy)
        g = g.max() * g

        return g

    elif algo_type == 1:
        print("algorithm_1 called")
        # Algorithm based on 1D Convolution
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        img_b = cv2.GaussianBlur(img, (3, 3), 0)  # reduce high frequency noise

        gx1 = np.array((1, 2, 1))  # vertical
        gx2 = np.array((-1, 0, 1))
        gy1 = np.array((-1, 0, 1))  # vertical
        gy2 = np.array((1, 2, 1))
        gx1 = gx1.reshape(3, 1)
        gy1 = gy1.reshape(3, 1)

        b = one_d(img_b, gy1, gy2)
        a = one_d(img_b, gx1, gx2)
        c = np.sqrt(a * a + b * b)
        return c

    elif algo_type == 3:
        # External filter code 3
        print("algorithm_3 called")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return algorithm_3(img)

    elif algo_type == 4:
        # External filter code 4
        print("algorithm_4 called")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return algorithm_4(img)

    elif algo_type == 5:
        # External filter code 5
        print("algorithm_5 called")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return algorithm_5(img)
