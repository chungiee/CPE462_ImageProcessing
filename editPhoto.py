from tkinter import *
import math
from PIL import ImageTk
from PIL import Image
from editFunctions import LucyRestoration, histogramEqualize, sharpenPic, blurPic, rotateCounter, rotateClock, cropPic, \
    sketchPic, oilPic, pencilPic, foilPic, negativePic
from canny_edges import cannyEdges


def changeImage(counter):
    img = ImageTk.PhotoImage(Image.open('image' + str(counter) + '.jpg'))
    panel.configure(image=img)
    panel.image = img


def sharpenImgFunc():
    global counter
    curImg = 'image' + str(counter) + '.jpg'
    counter = counter + 1
    sharpenPic(curImg, counter)
    changeImage(counter)


def blurImgFunc():
    global counter
    curImg = 'image' + str(counter) + '.jpg'
    counter = counter + 1
    blurPic(curImg, counter)
    changeImage(counter)


def rotateCounterFunc():
    global counter
    curImg = 'image' + str(counter) + '.jpg'
    counter = counter + 1
    rotateCounter(curImg, counter)
    changeImage(counter)


def rotateClockFunc():
    global counter
    curImg = 'image' + str(counter) + '.jpg'
    counter = counter + 1
    rotateClock(curImg, counter)
    changeImage(counter)


def cropImgFunc():
    global counter
    curImg = 'image' + str(counter) + '.jpg'
    counter = counter + 1
    cropPic(curImg, counter)
    changeImage(counter)


def undoFunc():
    global counter
    if counter > 0:
        counter = counter - 1
    changeImage(counter)


def sketchImgFunc():
    global counter
    curImg = 'image' + str(counter) + '.jpg'
    counter = counter + 1
    sketchPic(curImg, counter)
    changeImage(counter)


def oilImgFunc():
    global counter
    curImg = 'image' + str(counter) + '.jpg'
    counter = counter + 1
    oilPic(curImg, counter)
    changeImage(counter)


def paintImgFunc():
    global counter
    curImg = 'image' + str(counter) + '.jpg'
    counter = counter + 1
    pencilPic(curImg, counter)
    changeImage(counter)


def foilImgFunc():
    global counter
    curImg = 'image' + str(counter) + '.jpg'
    counter = counter + 1
    foilPic(curImg, counter)
    changeImage(counter)


def negativeImgFunc():
    global counter
    curImg = 'image' + str(counter) + '.jpg'
    counter = counter + 1
    negativePic(curImg, counter)
    changeImage(counter)


def histogramEqualizationFunc():
    global counter
    curImg = 'image' + str(counter) + '.jpg'
    counter = counter + 1
    histogramEqualize(curImg, counter)
    changeImage(counter)


def LucyRestorationFunc():
    global counter
    curImg = 'image' + str(counter) + '.jpg'
    counter = counter + 1
    LucyRestoration(curImg, counter)
    changeImage(counter)

def cannyEdgeDetectionFunc():
    global counter
    curImg = 'image' + str(counter) + '.jpg'
    counter = counter + 1
    cannyEdges(curImg, counter)
    changeImage(counter)


main = Tk()
counter = 0
main.title("Photo Editor")
main.geometry("1800x1000")
var = IntVar()
editingBox = Frame(main)

undoButton = Button(main, text="Undo", command=undoFunc, font=20)
undoButton.pack(side=BOTTOM, pady=10)

formatLabel = Label(editingBox, text="Format", font=16)
formatLabel.pack(side=TOP, pady=10)

SharpenButton = Button(editingBox, text="Sharpen Image", command=sharpenImgFunc, width=20)
SharpenButton.pack(side=TOP)
BlurButton = Button(editingBox, text="Blur Image", command=blurImgFunc, width=20)
BlurButton.pack(side=TOP)
CropButton = Button(editingBox, text="Crop", command=cropImgFunc, width=20)
CropButton.pack(side=TOP)
rotateCounterButton = Button(editingBox, text="Rotate Counter Clockwise", command=rotateCounterFunc, width=20)
rotateCounterButton.pack(side=TOP)
rotateClockButton = Button(editingBox, text="Rotate Clockwise", command=rotateClockFunc, width=20)
rotateClockButton.pack(side=TOP)

# img = ImageTk.PhotoImage(Image.open('image' + str(counter) + '.jpg'))
pre_img = Image.open('image' + str(counter) + '.jpg')
if pre_img.width > 850 or pre_img.height > 500:
    (width, height) = (math.floor(pre_img.width / 1.1), math.floor(pre_img.height / 1.1))
    pre_img = pre_img.resize((width, height))
    pre_img.save('image' + str(counter) + '.jpg')
img = ImageTk.PhotoImage(pre_img)

panel = Label(main, image=img)
panel.pack(side=LEFT, padx=20)

panel = Label(main, image=img)
panel.pack(side=LEFT, padx=20)

histogramButton = Button(editingBox, text="Canny Edge Detection", command=cannyEdgeDetectionFunc, width=20)
histogramButton.pack(side=BOTTOM)
histogramButton = Button(editingBox, text="Histogram equalization", command=histogramEqualizationFunc, width=20)
histogramButton.pack(side=BOTTOM)
restorationButton = Button(editingBox, text="Lucy-Richardson restoration", command=LucyRestorationFunc, width=20)
restorationButton.pack(side=BOTTOM)
negativeButton = Button(editingBox, text="Photo negative", command=negativeImgFunc, width=20)
negativeButton.pack(side=BOTTOM)
foilButton = Button(editingBox, text="Foil art", command=foilImgFunc, width=20)
foilButton.pack(side=BOTTOM)
pencilButton = Button(editingBox, text="Sharp paint", command=paintImgFunc, width=20)
pencilButton.pack(side=BOTTOM)
oilButton = Button(editingBox, text="Oil paint", command=oilImgFunc, width=20)
oilButton.pack(side=BOTTOM)
sketchButton = Button(editingBox, text="Sketch light", command=sketchImgFunc, width=20)
sketchButton.pack(side=BOTTOM)
filterLabel = Label(editingBox, text="Filters", font=16)
filterLabel.pack(side=BOTTOM, pady=10)

editingBox.pack()
main.mainloop()
