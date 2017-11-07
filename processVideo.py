#Process video with opencv
from multiprocessing import Process
import numpy as np
import cv2

#file manager: takes care of the file system
def fManager():
    print "I'm the manager :D"

#video manager: takes care of a single video stream
def vidThread(handle):
    print "I handle video from",handle

if __name__ == '__main__':
    #Get the camera addresses from config.dat
    cameraList = open("config.dat", "r")
    cameras = cameraList.readlines()
    cameras = map(str.strip, cameras)
    
     #split into processes, 1 per feed + a file manager
    threads = []
    #make and start the file manager
    threads.append(Process(target=fManager))
    threads[0].start()
    
    #Attatch video handlers to each camera
    vidHandle = []
    for i in range(1,len(cameras)):
        vidHandle.append(cv2.VideoCapture(i))
        print "got",i
        threads.append(Process(target=vidThread, args=(vidHandle[i-1])))
        threads[i].start()

   
