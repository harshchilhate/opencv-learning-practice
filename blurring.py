import numpy as np
import argparse 
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required= True, help= "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Orignal", image)

#Average Blur: Smooths an image by replacing each pixel with the average value of its neighborhood
#using a normalized box filter.
blurred = np.hstack([cv2.blur(image, (3, 3)),
                     cv2.blur(image, (5, 5)),
                     cv2.blur(image, (7, 7))])
cv2.imshow("Averaged Blur", blurred)
cv2.waitKey(0)

#Gaussian Blur : Reduces noise by applying a weighted average based on a Gaussian distribution, 
#giving more weight to closer pixels for a natural, soft blur.
blurred = np.hstack([cv2.GaussianBlur(image, (3, 3), 0),
                     cv2.GaussianBlur(image, (5, 5), 0),
                     cv2.GaussianBlur(image, (7, 7), 0)])
cv2.imshow("Gaussian Blur", blurred)
cv2.waitKey(0)

#Median Blur : Effectively removes salt-and-pepper noise by replacing each pixel with the median value of its neighborhood, 
#preserving edges better than mean blurring.
blurred = np.hstack([cv2.medianBlur(image, 3),
                     cv2.medianBlur(image, 5),
                     cv2.medianBlur(image, 7)])
cv2.imshow("Median Blur", blurred)
cv2.waitKey(0)

#Bilateral Blur : Removes noise while strongly preserving sharp edges by considering both 
#spatial proximity and pixel intensity similarity. 
blurred = np.hstack([cv2.bilateralFilter(image, 5, 21, 21),
                     cv2.bilateralFilter(image, 7, 31, 31),
                     cv2.bilateralFilter(image, 9, 41, 41)])
cv2.imshow("Bilateral Blur", blurred)
cv2.waitKey(0)

cv2.destroyAllWindows()