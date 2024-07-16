import numpy as np
import cv2

background = (
    np.ones((600, 1200, 3), np.uint8) * 255
)
sub_image1 = cv2.imread("./puzzle/img1.png")
sub_image2 = cv2.imread("./puzzle/img2.png")
sub_image3 = cv2.imread("./puzzle/img3.png")
sub_image4 = cv2.imread("./puzzle/img4.png")
sub_image5 = cv2.imread("./puzzle/img5.png")
sub_image6 = cv2.imread("./puzzle/img6.png")
sub_image7 = cv2.imread("./puzzle/img7.png")
sub_image8 = cv2.imread("./puzzle/img8.png")
sub_image9 = cv2.imread("./puzzle/img9.png")
sub_image10 = cv2.imread("./puzzle/img10.png")
sub_image11 = cv2.imread("./puzzle/img11.png")
sub_image12 = cv2.imread("./puzzle/img12.png")
sub_image13 = cv2.imread("./puzzle/img13.png")
sub_image14 = cv2.imread("./puzzle/img14.png")
sub_image15 = cv2.imread("./puzzle/img15.png")
sub_image16 = cv2.imread("./puzzle/img16.png")
sub_image17 = cv2.imread("./puzzle/img17.png")
sub_image18 = cv2.imread("./puzzle/img18.png")

def place(row, col, sub_image):
    x1 = (col - 1) * sub_image.shape[1]
    x2 = x1 + sub_image.shape[1]
    y1 = (row - 1) * sub_image.shape[0]
    y2 = y1 + sub_image.shape[0]
    background[y1:y2, x1:x2] = sub_image

def resize(sub_image):
    img = cv2.resize(sub_image, (200, 200))
    img = cv2.addWeighted(img, 1.5, np.zeros(img.shape, img.dtype), 0, 0)
    return img


def flip(sub_image):
    return cv2.flip(sub_image, 1)

def rotate_image(image, angle):
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result


sub_image1 = resize(sub_image1)
sub_image2 = resize(sub_image2)
sub_image3 = resize(rotate_image(sub_image3, -45))
sub_image4 = resize(rotate_image(sub_image4, -72))
sub_image5 = resize(rotate_image(sub_image5, -90))
sub_image6 = flip(resize(rotate_image(sub_image6, 90)))
sub_image7 = flip(resize(sub_image7))
sub_image8 = resize(sub_image8)
sub_image9 = flip(resize(sub_image9))
sub_image10 = resize(sub_image10)
sub_image11 = resize(rotate_image(sub_image11, -100))
sub_image12 = resize(sub_image12)
sub_image13 = resize(rotate_image(sub_image13, -45))
sub_image14 = resize(sub_image14)
sub_image15 = resize(sub_image15)
sub_image16 = resize(sub_image16)
sub_image17 = resize(rotate_image(sub_image17, 90))
sub_image18 = resize(sub_image18)

place(1, 1, sub_image1)
place(3, 4, sub_image2)
place(2, 2, sub_image3)
place(1, 4, sub_image4)
place(1, 2, sub_image5)
place(2, 3, sub_image6)
place(2, 1, sub_image7)
place(2, 5, sub_image8)
place(2, 4, sub_image9)
place(3, 1, sub_image10)
place(1, 6, sub_image11)
place(3, 6, sub_image12)
place(2, 6, sub_image13)
place(1, 5, sub_image14)
place(3, 3, sub_image15)
place(3, 2, sub_image16)
place(3, 5, sub_image17)
place(1, 3, sub_image18)

cv2.imwrite("complete_image.jpg", background)
cv2.destroyAllWindows()
