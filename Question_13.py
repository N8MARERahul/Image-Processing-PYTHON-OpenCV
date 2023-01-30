import cv2
import numpy as np

# Load the image
img = cv2.imread("images\image1.jpeg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding
_, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

# Display the image
cv2.imshow("Thresholded Image", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()