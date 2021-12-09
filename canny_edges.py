import cv2 as cv
import tkinter as tk
from PIL import Image, ImageFilter, ImageOps

def cannyEdges(curImg, counter):
    current = cv.imread(curImg)
    newImg = cv.Canny(current, 125, 175)
    cv.imwrite('image' + str(counter) + '.jpg', newImg)