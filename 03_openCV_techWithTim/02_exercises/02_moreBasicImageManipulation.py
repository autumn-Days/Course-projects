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

def addNoise(img):
    for i in range(50):
        for j in range(len(img[i])):
            img[i][j] = random.randint(0,250)

def move(img,part1:List[List, List], part2:List[List, List]):
    temp = part1
    
    img[part1[0], part1[1]] = img[part2[0], part2[1]]
    img[part2[0], part2[1]] = img[temp[0], temp[1]]

    


img = cv2.imread("../01_imgs/trees.jpg",1)
print(img.shape) #(430, 1450)
addNoise(img)
move(img, [])
cv2.imwrite("output2.jpg", img)