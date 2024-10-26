"""
##Values to represent pixels

-The images are treated by openCV as being tridimensional array

print(image.size())

Those are the rows of the images
[
    [],
    [],
    [],
]

Those are rows plus the columns
[
    [[],[],[]],
    [[],[],[]],
    [[],[],[]]
]

[0,255,0] : 0% blue, 100% green, 0% red

print(img.shape) => (height,width, amoutOfChannels)
    - the channel is just the color space of the image

example of a 2x2 image

[
    [[0,0,0],[255,255,255]],
    [[0,0,0],[255,255,255]]
]
"""
import cv2
import random
from typing import *

class MatrixSlice():
    def __init__(self,startLine, endLine, startColumn, endColumn):
        self.startLine = startLine
        self.endLine = endLine
        self.startColumn = startColumn
        self.endColumn = endColumn

def addNoise(img):
    for i in range(50):
        for j in range(len(img[i])):
            img[i][j] = random.randint(0,250)

def swap(img, fst:MatrixSlice, snd:MatrixSlice):
    temp = img[fst.startLine:fst.endLine, fst.startColumn:fst.endColumn].copy()
    img[fst.startLine:fst.endLine, fst.startColumn:fst.endColumn] = img[snd.startLine:snd.endLine, snd.startColumn:snd.endColumn]
    img[snd.startLine:snd.endLine, snd.startColumn:snd.endColumn] = temp

img1 = cv2.imread("../01_imgs/trees.jpg",1)
img2 = cv2.imread("../01_imgs/trees.jpg",1)
print(img1.shape) #(430, 1450, 3)


addNoise(img1)
firstPiece = MatrixSlice(320,400,1300,1380)
secondPiece = MatrixSlice(1,81,1,81)
swap(img2, firstPiece, secondPiece)

cv2.imwrite("output2.jpg", img1)
cv2.imwrite("output3.jpg", img2)