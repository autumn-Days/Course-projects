import cv2

"""
imread(<fileName>.<extension>):
    -Is used to open images
    -Wont load the image in RGB, but instead will load it BGR
    -The image can be loaded in three different ways:
        - cv2.IMREAD_GRAYSCALE: in gray scale. (0)
        - cv2.IMREAD_UNCHANGED: with the regular BGR (1)
        - cv2.IMREAD_COLOR: without considering transparency of the image (if the image is transparent) (or -1)

cv2.imshow(<windowName>, <image>)
cv2.imwrite(<fileName>.<extension>, <image>)
cv2.waitKey(<secs>):
    -It will wait for a certain amount of seconds for the window to be closed
    -If the option is 0, then it will wait an infinite amount of time for you to press any key on the keyboard
cv2.destroyAllWindows():
    - destroy all imagens

cv2.resize(<image>, (width,height))
cv2.resize(<image>, (0,0), fx=<widthProportion>, fy=<heightProportion>)
    -To resize with proportion

cv2.rotate(<image>, <rotationMode>)
cv2.rotate(<image>, cv2.cv2.ROTATE_90_CLOCKWISE)
"""
img = cv2.imread("../01_imgs/trees.jpg",0)
#cv2.imshow("myImage", img)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
cv2.imwrite("output.jpg", img)
print("It worked!")