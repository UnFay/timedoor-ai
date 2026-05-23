import cv2
import numpy as np
img = cv2.imread("exercise.jpg")

#shapes
cv2.rectangle(img, (300,30), (430,150), (0, 255, 0), 3)
cv2.rectangle(img, (400, 250), (600,380), (0, 0, 255), 3)
cv2.circle(img, (380,370), 50, (255,0,0), 3)

#text
img = cv2.putText(img, "Guy", (300, 20),
cv2.FONT_HERSHEY_COMPLEX, 1 , (0,255,0), 2)
img = cv2.putText(img, "Laptop", (400, 240),
cv2.FONT_HERSHEY_COMPLEX, 1 , (0,0,255), 2)
img = cv2.putText(img, "Mug", (330, 310),
cv2.FONT_HERSHEY_COMPLEX, 1 , (255,0,0), 2)

#display
cv2.imshow("Picher", img)
cv2.waitKey(0)
cv2.destroyAllWindows