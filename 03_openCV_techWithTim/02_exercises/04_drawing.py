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

def drawCirle(frame, center:Tuple[int,int], radius, color:Tuple[int, int, int], thickness):
    """
    the circle takes the center position and the radious
    """
    return cv2.circle(frame, center, radius, color, thickness)

def writeText(frame, message:str, bottonLeft:Tuple[int, int]):
    fontFamily = cv2.FONT_HERSHEY_SIMPLEX
    fontSize = 1
    fontColor = (255,0,255)
    fontThickness = 2
    fontScale = 1
    return cv2.putText(frame, message, bottonLeft, fontFamily, fontSize, fontColor, fontThickness, cv2.LINE_AA)

def display(frame):
        cv2.imshow("Camera", frame)
  
capture = cv2.VideoCapture(0)
width = getWidth(capture)
height = getHeight(capture)
print(f"width:{width}\nheight{height}")

while True:
    ret, frame = capture.read()
    """
    Since those drawings are inside a loop, it gives the impression the shapes
    are being drawn at the same time, but this is not really the case.
    """
    display(drawLine(frame,(0,0), (width,height), (0,0,255), 5))
    display(drawLine(frame,(0,height), (width,0), (255,0,0), 5))
    display(drawRectangle(frame,(0,240), (250,400), (0,255,0), -1)) #-1 to fill the shape
    display(drawCirle(frame, (300, 300), 100, (100,100,0), 5))
    display(writeText(frame,"hello!", (200,150)))
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()