# Write a program to enhance the image in spatial domain using histogram equalization method.
import numpy as np
import cv2

image = cv2.imread("images\image2.jpeg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

eqilization = cv2.equalizeHist(image)

cv2.imshow("Histogram Equilization", np.hstack([image, eqilization]))

cv2.waitKey(0)