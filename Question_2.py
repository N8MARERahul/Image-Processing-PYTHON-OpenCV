# Write a program to read an image and rotate that image in clockwise and anti-clockwise direction, and display it.

import numpy as np
import cv2

image = cv2.imread("images\image1.jpeg")
cv2.imshow("Original Image -->", image)

(h, w) = image.shape[ : 2]
center = (w // 2, h // 2)
m = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated_clockwise = cv2.warpAffine(image, m, (w, h))
cv2.imshow("Clockwise Rotated Image -->", rotated_clockwise)

M = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated_anti_clockwise = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Anti-Clockwise Rotated Image -->", rotated_anti_clockwise)

cv2.waitKey(0)