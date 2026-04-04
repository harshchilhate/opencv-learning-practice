import numpy as np 
import argparse 
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required= True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (11, 11), 0)

cv2.imshow("Orignal", image)

edged = cv2.Canny(blurred, 30, 150)
cv2.imshow("Edges", edged)

contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(f"I count {len(contours)} coins in the image")

coins = image.copy()
cv2.drawContours(coins, contours, -1, (0, 0, 0))
cv2.imshow("Coins", coins)

for (i, c) in enumerate(contours):
    (x, y, w, h) = cv2.boundingRect(c)

    print(f"Coin #{i + 1}")
    coin = image[y:y + h, x:x + w]
    cv2.imshow(f"Coin #{i + 1}", coin)

    mask = np.zeros(image.shape[:2], dtype= "uint8")
    ((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
    cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
    mask = mask[y:y +h, x:x +w]
        
    cv2.imshow(f"Masked Coin #{i + 1}", cv2.bitwise_and(coin, coin, mask= mask))

cv2.waitKey(0)
cv2.destroyAllWindows
