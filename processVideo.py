#Process video with opencv
import numpy as np
#import cv2

cameraList = open("config.dat", "r")
cameras = cameraList.readlines()
cameras = map(str.strip, cameras)

#vidHandle = cv2.VideoCapture('pull in login info from configured .gitignore file')
