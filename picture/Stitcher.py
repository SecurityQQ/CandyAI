import json
import numpy
import cv2
import math
import sys
import features
import random
from collections import deque

INDEX_PATH = "./index/"
IMAGES_TO_USE_PER_IMAGE = 5

def readIndex():
    json_data = open(INDEX_PATH + "histogram.index").read()
    return json.loads(json_data)

def preparInputImage(path, tileSize):
    i = cv2.imread(path)
    (h, w, _) = i.shape
    i = cv2.resize(i, (int(w / tileSize * tileSize), int(h / tileSize * tileSize)))
    return i

def preparePatch(path, tileSize):
    image = cv2.imread(INDEX_PATH + path)
    image = cv2.resize(image, (tileSize, tileSize))
    return image

def calcDistance(fts1, fts2, vectors):
    distance = 0
    for vec in vectors:
        distance += math.pow(fts1[vec] - fts2[vec], 2)
    return math.sqrt(distance)

def getIndexImage(fts, index, vectors):
    minDistance = 65000
    bestImages = deque([])
    for item in index:
        distance = calcDistance(fts, item, vectors)
        if distance < minDistance:
            minDistance = distance
            bestImages.append(item["file"])
            if len(bestImages) > IMAGES_TO_USE_PER_IMAGE:
                bestImages.popleft();

    return random.choice(bestImages)

def processLine(i, w, index, inputImage, tileSize, channels):
    for j in range(0, int(w / tileSize)):
        roi = inputImage[i * tileSize:(i + 1) * tileSize, j * tileSize:(j + 1) * tileSize]
        fts = features.extractFeature(roi)
        patch = preparePatch(getIndexImage(fts, index, channels), tileSize)
        inputImage[i * tileSize:(i + 1) * tileSize, j * tileSize:(j + 1) * tileSize] = patch
        cv2.imshow("Progress", inputImage)
        cv2.waitKey(1)


def main():
    
    params=sys.argv
    if len(sys.argv) < 5:
        params=['', 'filename1.jpg', '10', 'rgb', 'mymosaic.jpg']
        
    #parse commandline arguments
    inputImagePath = str(params[1])
    tileSize = int(params[2])
    channels = list(str(params[3]))
    
    #read index + input image
    index = readIndex()
    inputImage = preparInputImage(inputImagePath, tileSize)
        
    (h, w, _) = inputImage.shape
     
    inputImage = cv2.resize(inputImage, (int(w / tileSize * tileSize), int(h / tileSize * tileSize)))
    print (inputImage.shape)
      
    for i in range(0, int(h / tileSize)):
        processLine(i, w, index, inputImage, tileSize, channels)
        
    print ("Finished processing of image")
     
    
    cv2.imwrite(str(params[4]), inputImage)

    from PIL import Image                                                                                
    img = Image.open('mymosaic.jpg')
    img.show() 
     
     
if __name__ == "__main__":
    main()

main()