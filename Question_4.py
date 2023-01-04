# Write a program to perform color separation into R, G, and B from an color image.

import cv2
import numpy as np

image = cv2.imread("images\image4.jpeg")
cv2.imshow("Original Image", image)
cv2.waitKey(0)

b, g, r = cv2.split(image)

cv2.imshow("Red", r)
cv2.waitKey(0)
cv2.imshow("Green", g)
cv2.waitKey(0)
cv2.imshow("Blue", b)
cv2.waitKey(0)

cv2.waitKey(0)