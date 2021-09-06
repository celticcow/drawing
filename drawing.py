#!/usr/bin/python3

import numpy as np
import imageio
import cv2
import scipy.ndimage

"""
pip3 install watchdog
pip3 install numpy
pip3 install imageio
pip3 install cv
pip3 install scipy
sudo apt-get install python3-opencv
sudo apt-get install python3-scipy
pip3 install stsci.ndimage

"""

def grayscale(rgb):
    return(np.dot(rgb[...,:3],[0.299,0.587,0.144]))

def dodge(front,back):
    result = front*255/(255-back)
    result[result>255]=255
    result[back==255]=255

    return(result.astype('uint8'))

def main():
    debug = 1
    img = "image.jpeg"

    s = imageio.imread(img)
    g = grayscale(s)
    i = 250-g

    b = scipy.ndimage.filters.gaussian_filter(i,sigma=10)
    r = dodge(b,g)

    if(debug == 1):
        print(img)
        print("-"*20)
        print(r)
        print("end")

    cv2.imwrite('2.png',r)
#end of main

if __name__ == "__main__":
    main()
#end of program