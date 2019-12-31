import cv2
import numpy as np


image = cv2.imread("fat_circles.PNG")


hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red = np.array([63, 71, 204])
upper_red = np.array([255, 255, 255])

mask = cv2.inRange(hsv, lower_red, upper_red)


cv2.imshow("Original Image", image)

cv2.imshow("Detection", mask)

cv2. waitKey(0)
cv2.destroyAllWindows()
