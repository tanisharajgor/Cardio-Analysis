#This program is to train it btw: you need to import sklearn
from sklearn.datasets import load_breast_cancer
import numpy as np #idk why this greyed out


#the example I used had you import the data from a library,
#but we could just input our own data into it. The more we find the better to make it very accurate.

#just osme other things from the library to help with the detection
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


# Load dataset (once again we need to import it from our end
data = load_breast_cancer()

#you can write it in a separate header file (which you can then import) such as this (not real values in the arrays btw)
# https://www.tutorialspoint.com/python/python_further_extensions.htm (You need to use C as an extension tho, but its not too difficult to implement)
# tau = np.array([63, 71, 204])
# amyb = np.array([255, 255, 255])

# Organize our data
label_names = data['target_names']
labels = data['target']
feature_names = data['feature_names']
features = data['data']

# Look at our data
print(label_names)
print('Class label = ', labels[0])
print(feature_names)
print(features[0])

# Split our data
# might need to change the number depending on the sample size
train, test, train_labels, test_labels = train_test_split(features,
                                                          labels,
                                                          test_size=0.33,
                                                          random_state=42)

# Initialize our classifier
gnb = GaussianNB()

# Train our classifier based on what the parameters for amyloid beta values are
model = gnb.fit(train, train_labels)

# Make predictions
preds = gnb.predict(test)
print(preds)

# You might actually want to integrate your part before this
# basically how it all fits.

# Evaluate accuracy
print(accuracy_score(test_labels, preds))

#this applies what it learns to actually say whether you are in danger or not
## idk if we want to do an array or a single number for the tau protein frequency and amy-b values

#i liked your old program which asked the questions to help determine it or we could use this to distinguish between diseases (these symptoms are real).
#depends on the data/parameters we have
if amyb >= (1, 2, 3) && tau >= (1, 2, 3):
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
        print("It is best recommended for you to meet a doctor.")
    else:
        print("You are showing signs but indicating only a few internal ones, it seems as though")
        print("Whatever else should be here.")


else:
    print("You're good")



