# Write a program to enhance the image in spatial domain using –
# a) Image negative
# b) Log transformation
# c) Power law transform
# d) Piecewise linear transform

import cv2
import numpy as np

image = cv2.imread("images/image3.jpeg")
cv2.imshow("Original Image", image)

# a) Image negative...
image_negative = 255 - image
cv2.imshow("Negative Image", image_negative)
cv2.waitKey(0)

# b) Log Transformation...
img = cv2.imread("images/fourier_spectrum.png")
cv2.imshow("Original Image", img)
c = 255/(np.log(1 + np.max(img)))
log_transformed = c * np.log(1 + img)
log_transformed = np.array(log_transformed, dtype = np.uint8)
cv2.imshow("Log Tranceformation Image", log_transformed)
cv2.waitKey(0)

# c) Power law transformation...
img_2 = cv2.imread("images\image3.jpeg")
cv2.imshow("Original Image", img_2)
cv2.waitKey(0)
# Trying 4 gamma values.
for gamma in [0.1, 0.5, 1.2, 2.2]:
    gamma_corrected = np.array(255*(img_2 / 255) ** gamma, dtype = 'uint8')
    cv2.imshow(f"Power law transformed with exponent value = {gamma} .jpg", gamma_corrected)
    cv2.waitKey(0)
  
# d) Piecewise linear transformation...
# Function to map each intensity level to output intensity level.
def pixelVal(pix, r1, s1, r2, s2):
    if (0 <= pix and pix <= r1):
        return (s1 / r1)*pix
    elif (r1 < pix and pix <= r2):
        return ((s2 - s1)/(r2 - r1)) * (pix - r1) + s1
    else:
        return ((255 - s2)/(255 - r2)) * (pix - r2) + s2
# Open the image.
img = cv2.imread("images\image5.jpg")
# Define parameters.
r1 = 70
s1 = 0
r2 = 140
s2 = 255
# Vectorize the function to apply it to each value in the Numpy array.
pixelVal_vec = np.vectorize(pixelVal)
# Apply contrast stretching.
contrast_stretched = pixelVal_vec(img, r1, s1, r2, s2)
cv2.imshow("Original Image", img)
cv2.imshow("Contrast Stretched Image", contrast_stretched)
cv2.waitKey(0)