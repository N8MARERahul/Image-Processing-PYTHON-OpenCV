# Write a program to average two images together into a single image. Display the new image.

import cv2

image_1 = cv2.imread("images\image8_1.jpg")
image_2 = cv2.imread("images\image8_2.jpg")

average = cv2.addWeighted(image_1, 0.5, image_2, 0.5, 0)

cv2.imshow("First Image", image_1)
cv2.waitKey(0)
cv2.imshow("Second Image", image_2)
cv2.waitKey(0)
cv2.imshow("Average Image", average)
cv2.waitKey(0)