import numpy as np 
import argparse
import imutils
import cv2  

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required= True, help= "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Orignal", image)
cv2.waitKey(0)

resized = imutils.resize(image)
cv2.imshow("Resized via Function", resized)
cv2.waitKey(0)