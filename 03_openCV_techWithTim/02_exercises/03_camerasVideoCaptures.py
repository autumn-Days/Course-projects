"""
cv2.VideoCapture(<0-n>) :   it detects the camera you are using from the range of zero to one.
                            You can also specify the path to a video file and it will work just
                            as the same
"""

import numpy as np
import cv2

def initCanvas(frame):
    return np.zeros(frame.shape, np.uint8)

def divideCanvasByFour(capture, frame, canvas):
    width = int(capture.get(3)) #The parameter 3 specifies the width
    height = int(capture.get(4)) #The parameter 4 specifies the height
    frameDivided = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    #making the divisions
    canvas[height//2:, :width//2] = cv2.rotate(frameDivided, cv2.ROTATE_180)
    canvas[height//2:, width//2:] = cv2.rotate(frameDivided, cv2.ROTATE_180)
    canvas[:height//2, :width//2] = frameDivided
    canvas[:height//2, width//2:] = frameDivided
    
    cv2.imshow("frame", canvas)

#def divideVideoByFour():

capture = cv2.VideoCapture(0)

while True:
    """
    ret: a flag that indicates if the capture worked
    frame:The frame is the current image of the video itself (the numpy array which represents our image)
    """
    ret, frame = capture.read()
    canvas = initCanvas(frame)
    divideCanvasByFour(capture, frame, canvas)
    """
    it will wait 1 millisecond for the key
    to be 'q' key to be pressed. After that,
    it will exit keep with the execution.
    It ends the the loop if 'q' is pressed
    """
    if cv2.waitKey(1) == ord('q'):
        break

#Just say the camera can be used by other app
capture.release()
cv2.destroyAllWindows()
