import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2

colors = pd.read_csv('data\\pixel.csv')

feature_names = ['B', 'G', 'R']
X = colors[feature_names]
y = colors['Color']

# Partition the data into training and test data
from sklearn.model_selection import train_test_split
XTrain, XTest, yTrain, yTest = train_test_split(X,y,random_state=0)

from sklearn.tree import DecisionTreeClassifier

# Instantiate a decision tree classifier
knn = DecisionTreeClassifier()
knn.fit(XTrain, yTrain)
trainErr = knn.score(XTrain,yTrain)
testErr = knn.score(XTest,yTest)
print('Accuracy for training set: ')
print('Training Error: ',trainErr)
print('Testing Error: ',testErr)

# Choose test color
testColor = 'darkRed'
im = cv2.imread('testingColors\\' + testColor + '.png')
pixelTest = []
for y in im[1,1]:
    pixelTest.append(y)

# Print decision result
print(pixelTest)
print(knn.predict([pixelTest]))