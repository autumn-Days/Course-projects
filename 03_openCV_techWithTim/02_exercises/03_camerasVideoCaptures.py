"""
cv2.VideoCapture(<0-n>) :   it detects the camera you are using from the range of zero to one.
                            You can also specify the path to a video file and it will work just
                            as the same
"""

import numpy as np
import cv2

def createCanvas():
    image = np.zeros()

def divideVideoByFour():

capture = cv2.VideoCapture(0)

while True:
    """
    ret: a flag that indicates if the capture worked
    frame:The frame is the current image of the video itself (the numpy array which represents our image)
    """
    ret, frame = capture.read()
    cv2.imshow("frame", frame)

    #just exit the loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

#Just say the camera can be used by other app
capture.release()
cv2.destroyAllWindows()