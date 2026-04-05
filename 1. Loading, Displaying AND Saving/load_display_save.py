#how to load, display and save
import argparse #it is used in handling command-line arguments
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required= True, help= "Path to the image") # -i or --image is required input from user
args = vars(ap.parse_args()) #convert arguments into dictionary

image = cv2.imread(args["image"])

print("Width : {} Pixels".format(image.shape[1]))
print("Height : {} Pixels".format(image.shape[0]))
print("channels : {}".format(image.shape[2]))

cv2.imshow("Image", image) #show image in a window

#wait indefinitely until a key is pressed
cv2.waitKey(0)

cv2.imwrite("newimage.jpg", image) #saving image to disk in JPG format, OpenCV converts the format automatically based on the file extension you give in imwrite()