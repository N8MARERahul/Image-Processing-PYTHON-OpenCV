# Write a program to perform the following image enhancement methods.
# a) Brightness enhancement
# b) Brightness suppression
# c) Contrast manipulation
# d) Gray level slicing without background

import cv2

# a) Brightness enhancement
img = cv2.imread("images\image7.jpg") #load rgb image
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #convert it to hsv
value = 25
for x in range(0, len(hsv)):
    for y in range(0, len(hsv[0])):
        hsv[x, y][2] += value

img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow("image_processed.jpg", img)
cv2.waitKey(0)