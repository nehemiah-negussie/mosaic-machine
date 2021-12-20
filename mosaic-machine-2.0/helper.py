import cv2 as cv
import numpy as np

# calculate average colour of image
def calculateColour(image):
    # resize to 1 pixel and get the BGR
    resized = cv.resize(image,(1,1))
    return [resized[0, 0, 0], resized[0,0,1], resized[0,0,2]] # return BGR

def searchLines(lines, original):
    best = ""
    best_score = 500 # the highest possible distance between two colors is sqrt(3 * 255^2) = ~442
    for line in lines:
        a = line.split()
        # euclidian distance
        distance  = np.sqrt(pow(int (a[1]) - original[0], 2) + pow(int (a[2]) - original[1], 2) + pow(int (a[3]) - original[2], 2))
        # only keep the lowest score
        if distance < best_score:
            best_score = distance
            best = a[0]
    return best