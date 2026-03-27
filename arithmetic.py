import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required= True, help= "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Orignal", image)

print(f"Max of 255: {cv2.add(np.array([[200]], dtype=np.uint8), np.array([[100]], dtype=np.uint8))}")
print(f"Min of 0: {cv2.subtract(np.array([[50]], dtype=np.uint8), np.array([[100]], dtype=np.uint8))}")

print(f"Wrap around (NumPy add): {np.uint8([200]) + np.uint8([100])}")
print(f"Wrap around (NumPy subtract): {np.uint8([50]) - np.uint8([100])}") 


M = np.ones(image.shape, dtype = "uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Added", added)
cv2.waitKey(0)

M = np.ones(image.shape, dtype = "uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtract", subtracted)
cv2.waitKey(0)