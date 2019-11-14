import cv2
import csv

# Current colors being added to data
colors = ['red', 'orange', 'yellow', 
    'green', 'blue', 'purple','black',
    'white', 'brown']
# Dark and light colors to improve classification
darkColors = ['red']
lightColors = []

csvData = [['Color', 'B', 'G', 'R']]

# Add base colors to data
for x in colors:
    imageName = 'trainingColors\\' + x + '.png'
    im = cv2.imread(imageName)
    pixelSet = [x]
    for y in im[1,1]:
        pixelSet.append(y)
    csvData.append(pixelSet)

# Add dark colors to data
for x in darkColors:
    imageName = 'trainingColors\\dark' + x + '.png'
    im = cv2.imread(imageName)
    pixelSet = [x]
    for y in im[1,1]:
        pixelSet.append(y)
    csvData.append(pixelSet)

# Add light colors to data
for x in lightColors:
    imageName = 'trainingColors\\light' + x + '.png'
    im = cv2.imread(imageName)
    pixelSet = [x]
    for y in im[1,1]:
        pixelSet.append(y)
    csvData.append(pixelSet)

# Write training data to CSV
with open('data\\pixel.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)
csvFile.close()