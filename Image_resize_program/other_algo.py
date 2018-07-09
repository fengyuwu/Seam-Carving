from scipy import ndimage

import cv2
# ndimage.sobel  cv2.Sobel cv2.Canny

def algorithm_3(open_img):
    return ndimage.sobel(open_img)


def algorithm_4(open_img):
    return cv2.Sobel(open_img, cv2.CV_8U, 1, 0, ksize=5)


def algorithm_5(open_img):
    return cv2.Canny(open_img, 100, 200)


#
# # 3
# open_img = cv2.imread('File1.jpg', 0)
# open_img = ndimage.sobel(open_img)
#
# cv2.imshow("Result Image with open cv", open_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# open_img = cv2.imread('File1.jpg', 0)
#
# # 4
# open_img = cv2.Sobel(open_img, cv2.CV_8U, 1, 0, ksize=5)
#
# cv2.imshow("Result Image with open cv", open_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# open_img = cv2.imread('File1.jpg', 0)
#
# # 5
# open_img = cv2.Canny(open_img, 100, 200)
#
# cv2.imshow("Result Image canny open cv", open_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
