# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 10:48:03 2019

@author: napra
"""

'''
Using OpenCV takes a video and produces a number of images.
Requirements
----
0You require OpenCV to be installed.
Run
---
Open the main.py and edit the path to the video. Then run:
$ python main.py
Which will produce a folder called data with the images.
'''

import cv2
import numpy as np
import os
from Testcode_1 import *

# Playing video from file:

cap = cv2.VideoCapture('KSTAR_003723_tv01.avi')

try:
    if not os.path.exists('data'):
        os.makedirs('data')

except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Saves image of the current frame in jpg file
    name = './data/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)
    # To stop duplicate images
    currentFrame += 1
    if not ret:
        break
# When everything done, release the capture

cap.release()

cv2.destroyAllWindows()