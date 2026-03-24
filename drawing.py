import numpy as np
import cv2

#building a blank canvas to draw on
canvas1 = np.zeros((300, 300, 3), dtype = "uint8") #np.zeros creates a black image

#drawing lines
green = (0, 255, 0)
cv2.line(canvas1, (0,0), (300, 300), green)
cv2.imshow("Canvas Lines", canvas1)
cv2.waitKey(0)

red = (0, 0, 255)
cv2.line(canvas1, (300,0), (0, 300), red, 3)
cv2.imshow("Canvas Lines", canvas1)
cv2.waitKey(0)

#drawing rectangle
canvas2 = np.zeros((300, 300, 3), dtype = "uint8")
cv2.rectangle(canvas2, (10,10), (60, 60), green)
cv2.imshow("Canvas rectangle", canvas2)
cv2.waitKey(0)

cv2.rectangle(canvas2, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas rectangle", canvas2)
cv2.waitKey(0)

blue = (255, 0, 0)
cv2.rectangle(canvas2, (200,50), (225, 125), blue, -1) #thickness = -1 means fill
cv2.imshow("Canvas rectangle", canvas2)
cv2.waitKey(0)

#drawing circle
canvas3 = np.zeros((300, 300, 3), dtype = "uint8")
(centerX, centerY) = (canvas3.shape[1]//2, canvas3.shape[0]//2)

white = (255, 255, 255)

for r in range(0, 175, 25):
    cv2.circle(canvas3, (centerX, centerY), r, white)

cv2.imshow("Canvas bullseye", canvas3)
cv2.waitKey(0)

canvas4 = np.zeros((300, 300, 3), dtype = "uint8")
for i in range(0, 25):
    radius = np.random.randint(5, high = 200)
    color = np.random.randint(0, high = 256, size = (3,)).tolist()
    pt = np.random.randint(0, high = 300, size = (2,))

    cv2.circle(canvas4, tuple(pt), radius, color, -1)

cv2.imshow("Canvas Art", canvas4)
cv2.waitKey(0) 