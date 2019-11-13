#import imageio
#import matplotlib.pyplot as plt
#from PIL import Image
import cv2
import csv

#pic = imageio.imread('greenPic.png')
#print(pic.shape)
#print(pic.size)
#print(pic.max())
#print(pic.min())
#print(pic[1,1,1])
colors = ['red', 'orange', 'yellow', 
    'green', 'blue', 'purple','black',
    'white', 'brown']

csvData = [['Color', 'B', 'G', 'R']]

for x in colors:
    imageName = 'trainingColors\\' + x + '.png'
    im = cv2.imread(imageName)
    pixelSet = [x]
    for y in im[1,1]:
        pixelSet.append(y)
    csvData.append(pixelSet)

with open('data\\pixel.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)
csvFile.close()