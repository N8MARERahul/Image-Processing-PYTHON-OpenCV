# Write a program to compare two images using image subtraction.
import cv2

image_1 = cv2.imread("images\image9_1.jpg")
image_2 = cv2.imread("images\image9_2.jpg")

compare_1 = cv2.subtract(image_2, image_1)
compare_2 = cv2.subtract(image_1, image_2)

compare = cv2.add(compare_1, compare_2)

cv2.imshow("First Image", image_1)
cv2.waitKey(0)
cv2.imshow("Second Image", image_2)
cv2.waitKey(0)
cv2.imshow("Compare", compare)
cv2.waitKey(0)