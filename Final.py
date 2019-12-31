import cv2
import numpy as np


img = cv2.imread('fs2.PNG', 0)
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

print(len(circles))

image = cv2.imread("fs2.PNG")


hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red = np.array([63, 71, 204])
upper_red = np.array([255, 255, 255])

mask = cv2.inRange(hsv, lower_red, upper_red)


# cv2.imshow("Original Image", image)

# cv2.imshow("Detection", mask)

if circles.shape >= (1, 2, 3):
    print("This picture has to many of discoloration marks. This is a sign of Heart Disease.")
    print("Answering the following questions will better help understand the situation")
    QA_a = input("Do you ever feel chest pain, chest tightness, chest pressure or chest discomfort?(Y/N) ")
    QA_b = input("Do you ever feel a shortness of breath?(Y/N) ")
    QA_c = input("Do you ever feel pain, numbness, weakness or coldness in your legs or arms?(Y/N) ")
    QA_d = input("Do you ever feel pain in the neck, jaw, throat, upper abdomen or back(Y/N) ")
    QA_e = input("Do you often faint, feel lightheaded, or dizzy ?(Y/N) ")
    result = 0
    if QA_a == "Y":
        result += 1
    else:
       result += 0

    if QA_b == "Y":
            result += 1
    else:
        result += 0
    if QA_c == "Y":
            result += 1
    else:
        result += 0
    if QA_d == "Y":
            result += 1
    else:
        result += 0
    if QA_e == "Y":
            result += 1
    else:
        result += 0
    if result >= 4:
        print("You have many signs showing and are also indicating many internal signs.")
        print("It is best recommended for you to meet a doctor.")
    else:
        print("You are showing signs but indicating only a few internal ones, it seems as though")
        print("The spots that developed on the bottom of your thumb may be a sign of a")
        print("heart infection called infective endocarditis.")



else:
    print("You're good")

cv2.waitKey(0)
cv2.destroyAllWindows()