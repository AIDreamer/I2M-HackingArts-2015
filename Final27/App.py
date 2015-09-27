__author__ = 'Son Pham'

from Tkinter import *
from tkFileDialog import askopenfilename
import Image, ImageTk
import pygame
import ImageToArray
import PIL
import ImageToSound

import time
from multiprocessing import Process

#Khai Nguyen
from cs5png import *

class Shape:

    def __init__(self,shapeID,x,y,musicID):
        self.shapeID = shapeID
        self.x = x
        self.y = y
        self.musicID = musicID

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getShapeID(self):
        return self.shapeID

    def getMusicID(self):
        return self.musicID

class Clickable:

    objectList = []
    count = 0

    def main(self):

        root = Tk()
        root.wm_title("I2M, an experimental music application")
        self.count = 1

        # Setting up a tkinter canvas with scrollbars
        frame = Frame(root, bd=2, relief=SUNKEN)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        #xscroll = Scrollbar(frame, orient=HORIZONTAL)
        #xscroll.grid(row=1, column=0, sticky=E+W)
        #yscroll = Scrollbar(frame)
        #yscroll.grid(row=0, column=1, sticky=N+S)
        #canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        canvas = Canvas(frame, bd=0)
        canvas.grid(row=0, column=0, sticky=N+S+E+W)
        #xscroll.config(command=canvas.xview)
        #yscroll.config(command=canvas.yview)
        frame.pack(fill=BOTH,expand=1)

        # Background image
        img = ImageTk.PhotoImage(Image.open("Background.gif"))
        canvas.create_image(0,0,image=img,anchor="nw")
        canvas.config(width = img.width(), height = img.height())

        # Adding the image
        File = askopenfilename(parent=root, initialdir="C:/",title='Choose an image.')
        # Preprocess array
        imageArray = ImageToArray.imageProcessing(File)

        img = ImageTk.PhotoImage(Image.open(File))
        canvas.create_image(0,0,image=img,anchor="nw")
        canvas.config(width = img.width(), height = img.height())
        # Canvas.config(scrollregion=canvas.bbox(ALL))

        #function to be called when mouse is clicked
        def hearMouseclick(event):
            print("1 click")
            # Grab x and y from even
            x = event.x
            y = event.y

            # Outputting x and y coords to console
            # print (x,y)

            # Delete circles that is already in the list
            check = False
            for shape in self.objectList:
                if (getdif(shape.getX(),x) < 10) and (getdif(shape.getY(),y) < 10):
                    canvas.delete(shape.getShapeID())
                    self.objectList.remove(shape)
                    check = True
                    ImageToSound.kill(shape.getMusicID())

            #draw a circle at that position
            if (check == False):
                self.draw_circle(canvas,event.x,event.y)
                ImageToSound.run(imageArray,x, y, self.count, 1)
                self.count += 1

        def hearDoubleclick(event):
            print("Double click")
            # Grab x and y from even
            x = event.x
            y = event.y

            # Delete circles that is already in the list
            check = False
            for shape in self.objectList:
                if (getdif(shape.getX(),x) < 10) and (getdif(shape.getY(),y) < 10):
                    canvas.delete(shape.getShapeID())
                    self.objectList.remove(shape)
                    check = True
                    ImageToSound.kill(shape.getMusicID())

            if (check == False):
                self.draw_circle(canvas,event.x,event.y)
                ImageToSound.run(imageArray,x, y, self.count, 3)
                self.count += 1

        def hearMotion(event):
            print("Double click")
            # Grab x and y from even
            x = event.x
            y = event.y

            # Delete circles that is already in the list
            check = False
            for shape in self.objectList:
                if (getdif(shape.getX(),x) < 10) and (getdif(shape.getY(),y) < 10):
                    canvas.delete(shape.getShapeID())
                    self.objectList.remove(shape)
                    check = True
                    ImageToSound.kill(shape.getMusicID())

            if (check == False):
                self.draw_circle(canvas,event.x,event.y)
                ImageToSound.run(imageArray,x, y, self.count, 3)
            pass


        #mouseclick event
        canvas.bind("<Button 1>",hearMouseclick)
        canvas.bind("<Double-Button-1>", hearDoubleclick)
        canvas.bind("<B1-Motion>", hearMotion)

        root.mainloop()

    def draw_circle(self, canvas, x, y):
        rad = 10
        circle = canvas.create_oval(x-rad ,y-rad, x+rad, y+rad, width=3, outline='#E3E2E0', stipple="gray50");
        # Add object to the list
        self.objectList.append(Shape(circle,x,y,self.count))

def getdif(a,b):
    return abs(a - b)

def play_music(music_file):
    """
    stream music with mixer.music module in blocking manner
    this will stream the sound from disk while playing
    """
    clock = pygame.time.Clock()
    try:
        pygame.mixer.music.load(music_file)
        print ("Music file %s loaded!")
    except pygame.error:
        print ("File %s not found! (%s)")
        return
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)

if __name__ == "__main__":
    app = Clickable()
    app.main()