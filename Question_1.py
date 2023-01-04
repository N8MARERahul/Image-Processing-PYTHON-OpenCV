# Write a program to do image format conversion 
# i.e., from RGB to gray, gray to binary, RGB to binary, RGB to HSV, HSV to RGB, RGB to YCbCr and YCbCr to RGB.

import cv2

image = cv2.imread("images\image3.jpeg")
cv2.imshow("Original Image", image)
cv2.waitKey(0)

# RGB to gray
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray_image)
cv2.waitKey(0)

# gray to binary
ret, binary_image = cv2.threshold(gray_image, 70, 255, 0)
cv2.imshow("Gray to Binary image", binary_image)
cv2.waitKey(0)

# RGB to binary
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
r, bin_image = cv2.threshold(gray_img, 70, 255, 0)
cv2.imshow("RGB to Binary Image", bin_image)
cv2.waitKey(0)

# RGB to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Image", hsv_image)
cv2.waitKey(0)

# HSV to RGB
hsv_to_rgb_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
cv2.imshow("HSV to RGB Image", hsv_to_rgb_image)
cv2.waitKey(0)

# RGB to YCbCr
ycbcr = cv2.cvtColor(image, cv2.COLOR_BGR2YCR_CB)
cv2.imshow("YCbCr Image", ycbcr)
cv2.waitKey(0)

# YCbcr to RGB
ycbcr_to_rgb_image = cv2.cvtColor(ycbcr, cv2.COLOR_YCrCb2BGR)
cv2.imshow("YCbCr to RGB Image", ycbcr_to_rgb_image)
cv2.waitKey(0)