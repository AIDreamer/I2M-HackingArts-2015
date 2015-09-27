#Khai Nguyen
from cs5png import *
import Image, ImageTk

def imageProcessing(filename):
    """ Run this function to read in the in.png image,
        change it, and write out the result to out.png.
    """

    im = Image.open(filename)
    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((1, 1))

    width = rgb_im.size[0]
    height = rgb_im.size[1]

    newPixels = [[rgb_im.getpixel((row,col)) for row in range(width)] for col in range(height)]
    # now, save to the file 'out.png'
    return newPixels


def scale(input):
    '''scale an image horizontal and vertical at the same time
       enter a string as the name of the input
    '''
    imagePixels=getRGB(input)
    def ver(s):
        return s[0::2]
    newPixels=[ver(row) for row in imagePixels]
    newPixels=newPixels[0::2]
    saveRGB(newPixels,'out.png')



                       

