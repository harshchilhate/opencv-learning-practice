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

M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted down and right", shifted)
cv2.waitKey(0)

M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted up and left", shifted)
cv2.waitKey(0)

