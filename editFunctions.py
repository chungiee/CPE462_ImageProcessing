from plot_deconvolution import Lucy_Restoration
from PIL import Image, ImageFilter, ImageOps
from PIL.ImageFilter import (
    BLUR, CONTOUR, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
    EMBOSS, FIND_EDGES, SHARPEN
)

import numpy as np

def sharpenPic(curImg, counter):
    current = Image.open(curImg)
    newImg = current.filter(SHARPEN)
    newImg.save('image' + str(counter) + '.jpg')


def blurPic(curImg, counter):
    current = Image.open(curImg)
    newImg = current.filter(BLUR)
    newImg.save('image' + str(counter) + '.jpg')


def rotateCounter(curImg, counter):
    newImg = Image.open(curImg)
    newImg.rotate(90).save('image' + str(counter) + '.jpg')


def rotateClock(curImg, counter):
    newImg = Image.open(curImg)
    newImg.rotate(270).save('image' + str(counter) + '.jpg')


def cropPic(curImg, counter):
    current = Image.open(curImg)
    width, height = current.size
    left = width / 4
    top = height / 4
    right = 3 * width / 4
    bottom = 3 * height / 4
    newImg = current.crop((left, top, right, bottom))
    newImg.save('image' + str(counter) + '.jpg')


def sketchPic(curImg, counter):
    current = Image.open(curImg)
    newImg = current.filter(CONTOUR)
    newImg.save('image' + str(counter) + '.jpg')


def oilPic(curImg, counter):
    current = Image.open(curImg)
    newImg = current.filter(EDGE_ENHANCE)
    newImg.save('image' + str(counter) + '.jpg')


def pencilPic(curImg, counter):
    current = Image.open(curImg)
    newImg = current.filter(EDGE_ENHANCE_MORE)
    newImg.save('image' + str(counter) + '.jpg')


def foilPic(curImg, counter):
    current = Image.open(curImg)
    newImg = current.filter(EMBOSS)
    newImg.save('image' + str(counter) + '.jpg')


def negativePic(curImg, counter):
    current = Image.open(curImg)
    newImg = current.filter(FIND_EDGES)
    newImg.save('image' + str(counter) + '.jpg')


def histogramEqualize(curImg, counter):
    current = Image.open(curImg)
    newImg = ImageOps.equalize(current, mask=None)
    newImg.save('image' + str(counter) + '.jpg')


def LucyRestoration(curImg, counter):
    current = Image.open(curImg)
    newImg = Lucy_Restoration(current)
    newImg.save('image' + str(counter) + '.jpg')

def histogramEqualize_2(curImg, counter):
     img = Image.open(curImg)
     # convert to grayscale
     img_gray = img.convert(mode='L')

     #convert to NumPy array
     img_array = np.asarray(img_gray)

     # PERFORM HISTOGRAM EQUALIZATION

     # STEP 1: Normalized cumulative histogram
     #flatten image array and calculate histogram via binning
     histogram_array = np.bincount(img_array.flatten(), minlength=256)

     #normalize
     num_pixels = np.sum(histogram_array)
     histogram_array = histogram_array/num_pixels

     #normalized cumulative histogram
     chistogram_array = np.cumsum(histogram_array)


     # STEP 2: Pixel mapping lookup table

     transform_map = np.floor(255 * chistogram_array).astype(np.uint8)

     #STEP 3: Transformation

     # flatten image array into 1D list
     img_list = list(img_array.flatten())

     # transform pixel values to equalize
     eq_img_list = [transform_map[p] for p in img_list]

     # reshape and write back into img_array
     eq_img_array = np.reshape(np.asarray(eq_img_list), img_array.shape)

     ######################################
     # WRITE EQUALIZED IMAGE TO FILE
     ######################################
     #convert NumPy array to pillow Image and write to file
     eq_img = Image.fromarray(eq_img_array, mode='L')
     eq_img.save('image' + str(counter) + '.jpg')