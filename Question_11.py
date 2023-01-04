# Write a program to add various types of noise (salt and pepper noise, Gaussian noise) to an image.

# Adding Gaussian noise...
import cv2
import numpy as np
img=cv2.imread("images\image3.jpeg")
cv2.imshow("Original",img)
blander3=np.hstack([cv2.GaussianBlur(img,(3,3),0)])
blander5=np.hstack([cv2.GaussianBlur(img,(5,5),0)])
blander7=np.hstack([cv2.GaussianBlur(img,(7,7),0)])
cv2.imshow("Gaussian noise 3x3",blander3)
cv2.imshow("Gaussian noise 5x5",blander5)
cv2.imshow("Gaussian noise 7x7",blander7)
cv2.waitKey(0)

# Adding salt and peeper noise...
import random

def add_noise(img):

	# Getting the dimensions of the image
	row , col = img.shape
	
	# Randomly pick some pixels in the
	# image for coloring them white
	# Pick a random number between 300 and 10000
	number_of_pixels = random.randint(300, 10000)
	for i in range(number_of_pixels):
	
		# Pick a random y coordinate
		y_coord=random.randint(0, row - 1)
		
		# Pick a random x coordinate
		x_coord=random.randint(0, col - 1)
		
		# Color that pixel to white
		img[y_coord][x_coord] = 255
		
	# Randomly pick some pixels in
	# the image for coloring them black
	# Pick a random number between 300 and 10000
	number_of_pixels = random.randint(300 , 10000)
	for i in range(number_of_pixels):
	
		# Pick a random y coordinate
		y_coord=random.randint(0, row - 1)
		
		# Pick a random x coordinate
		x_coord=random.randint(0, col - 1)
		
		# Color that pixel to black
		img[y_coord][x_coord] = 0
		
	return img

# salt-and-pepper noise can
# be applied only to grayscale images
# Reading the color image in grayscale image
img = cv2.imread("images\image8_1.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("Original Image", img)
cv2.imshow("Added slat and peeper noise", add_noise(img))
cv2.waitKey(0)