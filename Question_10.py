# Write a program to perform the following image_1 arithmetic.
# a) Image addition
# b) Image subtraction
# c) Image multiplication
# d) Image division

import cv2
import numpy as np

# a) Image addition
image_1 = cv2.imread("images\image6.jpg")
image_2 = cv2.imread("images\image7.jpg")
added = cv2.add(image_1, image_2)
cv2.imshow("Original Image 1", image_1)
cv2.imshow("Original Image 2", image_2)
cv2.waitKey(0)
cv2.imshow("Added Image", added)
cv2.waitKey(0)

# b) Image subtraction
sub = cv2.subtract(image_1, image_2)
cv2.imshow("Subtracted Image", sub)
cv2.waitKey(0)

# c) Image multiplication
mul = cv2.multiply(image_1, image_2)
cv2.imshow("Multiplied Image", mul)
cv2.waitKey(0)

# d) Image division
div = cv2.divide(image_1, image_2)
cv2.imshow("Divided Image", div)
cv2.waitKey(0)