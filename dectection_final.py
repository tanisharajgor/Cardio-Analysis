# import the necessary packages
from skimage import measure
import matplotlib.pyplot as plt
import numpy as np
import cv2


def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err


def compare_images(imageA, imageB, title):
    # compute the mean squared error and structural similarity
    # index for the images
    m = mse(imageA, imageB)
    s = measure.compare_ssim(imageA, imageB)
    # setup the figure
    fig = plt.figure(title)
    plt.suptitle("MSE: %.3f, SSIM: %.3f" % (m, s))
    # show first image
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap=plt.cm.gray)
    plt.axis("off")
    # show the second image
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap=plt.cm.gray)
    plt.axis("off")
    # show the images
    plt.show()

# load the images -- the original, the original + contrast,
# and the original + photoshop
test = cv2.imread("D4.jpg")
normal = cv2.imread("P1.jpg")
mild = cv2.imread("P2.jpg")
moderate = cv2.imread("P3.jpg")
severe = cv2.imread("P4.jpg")
# convert the images to grayscale
test = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)
normal = cv2.cvtColor(normal, cv2.COLOR_BGR2GRAY)
mild = cv2.cvtColor(mild, cv2.COLOR_BGR2GRAY)
moderate = cv2.cvtColor((moderate), cv2.COLOR_BGR2GRAY)
severe = cv2.cvtColor(severe, cv2.COLOR_BGR2GRAY)


# initialize the figure
fig = plt.figure("Images")
images = ("Test", test), ("Normal", normal), ("Mild", mild), ("Moderate", moderate), ("Severe", severe)
# loop over the images
for (i, (name, image)) in enumerate(images):
	# show the image
	ax = fig.add_subplot(1, 5, i + 1)
	ax.set_title(name)
	plt.imshow(image, cmap = plt.cm.gray)
	plt.axis("off")
# show the figure
plt.show()
# compare the images
compare_images(test, normal, "Test vs. Normal")
compare_images(test, mild, "Test vs. Mild")
compare_images(test, moderate, "Test vs. Moderate")
compare_images(test, severe, "Test vs. Severe")

print("Amyloid Beta and Tau Protein levels are irregular.")
print("Answering the following questions will better help understand the situation")
QA_a = input("Do you ever feel muscle weakness anywhere in the body?(Y/N) ")
QA_b = input("Do you ever feel a partial or complete loss of sensation?(Y/N) ")
QA_c = input("Have you ever had a seizure?(Y/N) ")
QA_d = input("Do you have blurry vision or slurred speech(Y/N) ")
QA_e = input("Do you often have a lack of coordination or balance?(Y/N) ")
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
    print("You may have severe dementia.")

if result == 3:
    print("You may have moderate damage.")


if result == 2:
    print("You are showing signs but indicating only a few internal ones, it seems as though you may have mild damage, check with a doctor.")

else:
    print("You're good!")
