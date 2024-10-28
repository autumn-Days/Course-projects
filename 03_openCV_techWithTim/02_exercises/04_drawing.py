"""
Cartesian plane in openCV. The "y" coordinate increases from top to down

(0,0)---------------------------------
|(0,1)
|(0,2)
|(0,3)
|(0,4)
|(0,5)
|(0,6)
|(0,7)
|(0,8)
|(0,9)
|(0,10)
"""


import numpy
import cv2
from typing import *

def getWidth(capture):
    return int(capture.get(3))

def getHeight(capture):
    return int(capture.get(4))

def drawLine(frame, init:Tuple[int, int], end:Tuple[int, int], color, thickness):
    return cv2.line(frame, init, end, color, thickness)

def drawRectangle(frame, topLeft:Tuple[int, int], bottonRight:Tuple[int,int], color, thickness):
    """
    For the rectangle the only thing that needs to be done is to pass the top left
    hand corner of the rectangle and the botton right corner of it
    """
    return cv2.rectangle(frame, topLeft, bottonRight, color, thickness)

def display(frame):
        cv2.imshow("Camera", frame)


    
capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    width = getWidth(capture)
    height = getHeight(capture)
    """
    Since those drawings are inside a loop, it gives the impression the shapes
    are being drawn at the same time, but this is not really the case.
    """
    display(drawLine(frame,(0,0), (width,height), (0,0,255), 5))
    display(drawLine(frame,(0,height), (width,0), (255,0,0), 5))
    display(drawRectangle(frame,(0,500), (250,750), (0,255,0), 5))

    if cv2.waitKey(1) == ord('q'):
        break

cv2.release()
cv2.destroyAllWindows() 
    