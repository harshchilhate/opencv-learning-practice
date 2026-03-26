import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype = "uint8")

box = 10  # size of each square

red = (0, 0, 255)

for i in range(300 // box):
    for j in range(300 // box):
        if (i + j) % 2 == 0:
            top_left_pixel = [i * box, j * box]
            bottom_right_pixel = [(i + 1) * box, (j + 1) * box]
            cv2.rectangle(canvas, tuple(top_left_pixel), tuple(bottom_right_pixel), red, -1)

green = (0, 255, 0)
(centerX, centerY) = (canvas.shape[1]//2, canvas.shape[0]//2)
cv2.circle(canvas, (centerX, centerY), 40, green, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)