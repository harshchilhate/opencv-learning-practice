import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required= True, help= "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Orignal", image)

#Note : OpenCV stores image in BGR format (NOT RGB)
(b, g, r) = image[0, 0]
print(f"Pixel at (0,0) - Red : {r}, Green : {g}, Blue : {b}")

image[0, 0] = (0, 0, 255) #set pixel at (0,0) to pure red
(b, g, r) = image[0, 0]
print(f"After change pixel at (0,0) - Red : {r}, Green : {g}, Blue : {b}")

corner = image[:100, :100] #extracting top-left 100 x 100 region
cv2.imshow("Image's top left corner", corner)

image[:100, :100] = (0, 255, 0) #setting region to green
cv2.imshow("Updated (green) image's top left corner", image) 
cv2.waitKey(0)