"""
• In order to detect the colors of an image, it is needed to use an image
of the format "hsv", because the method that detects colors expects this
type of input.

• Since by default we use BGR images, it is necessary to convert those images
to a hsv image
"""

import cv2

def convert2Hsv(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

capture = cv2.VideoCapture(0)
width = int(capture.get(3))
hwight = int(capture.get(4))

while True:
    ret, frame = capture.read()
    frame = convert2Hsv(frame)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == ord('q'):
        break
