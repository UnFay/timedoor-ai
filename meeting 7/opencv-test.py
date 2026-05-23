# run by typing python3 o [tab]
import cv2
import numpy as np
img = cv2.imread("avenger.jpg")
height, width, channel = img.shape
mask = np.zeros(img.shape[:2], dtype="uint8")
cv2.circle(mask, (160,200), 165, 255, -1)
img = cv2.bitwise_or(img, img, mask = mask)
# cv2.imshow("Mask", mask)
cv2.line(img, (0,0), (width, height), (0,255,0), 6)
cv2.line(img, (width, 0), (0,height), (0,255,0), 6)
cv2.rectangle(img, (0, 0), (width, 100), (0,255,0), -1)
img = cv2.putText(img, "Avengers!!", (100, 40),
cv2.FONT_HERSHEY_COMPLEX, 1 , (0,0,255), 2)
img = cv2.putText(img, "OpenCV", (100, height-30),
cv2.FONT_HERSHEY_COMPLEX, 1 , (255,255,255), 2)
red = ([0, 0, 30], [50, 56, 255])
blue = ([30,0, 0], [255, 150, 50])
green = ([0, 30, 0], [100, 255, 100])
white = ([255, 255, 255], [255, 255, 255])
boundaries = [red,blue,green,white]
for (lower, upper) in boundaries:
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
    mask = cv2.inRange(img, lower, upper)
    output = cv2.bitwise_and(img, img, mask = mask)
    cv2.imshow("Color Detection", output)
    cv2.waitKey(0)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows