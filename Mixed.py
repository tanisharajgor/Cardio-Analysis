import cv2
import numpy as np

img = cv2.imread('fs7.PNG', 0)
img = cv2.medianBlur(img, 5)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20,
                           param1=50, param2=30, minRadius=0, maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    # draw the outer circle
    cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle
    cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

# cv2.imshow("Original Image", img)

# cv2.imshow('detected circles', cimg)


image = cv2.imread("fs7.PNG")


hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red = np.array([165, 100, 102])
upper_red = np.array([255, 255, 255])

mask = cv2.inRange(hsv, lower_red, upper_red)


cv2.imshow("Original Image", image)

cv2.imshow("Detection", mask)

cv2. waitKey(0)
cv2.destroyAllWindows()






