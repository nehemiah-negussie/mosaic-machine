import cv2 as cv
import numpy as np
from PIL import Image
import scipy
import scipy.misc
import scipy.cluster

# Calculates the average colour of an image


def calculateColour(opencv_image):
    # Convert OpenCV image to PIL image
    opencv_image = cv.cvtColor(opencv_image, cv.COLOR_BGR2RGB)
    image = Image.fromarray(opencv_image)
    # Resizing for speed
    image = image.resize((150, 150))
    ar = np.asarray(image)
    shape = ar.shape
    ar = ar.reshape(scipy.product(shape[:2]), shape[2]).astype(float) 
    codes, _ = scipy.cluster.vq.kmeans(ar, 1)  # Calculate the 1 cluster (i.e dominant colour)
    dom = np.around(codes[0])
    return dom

# Search through all lines of text file


def searchLines(lines, original):
    # Set initial best values as worst possible so they will be overwritten
    best = ""
    best_score = 500  # The largest possible diff between two colors is ~442
    for line in lines:
        a = line.split()
        # Euclidian distance for BGR or RGB
        distance = np.sqrt(pow(int(a[1]) - original[0], 2) + pow(int(a[2]) - original[1], 2) + pow(int(a[3]) - original[2], 2))
        # Only keep the lowest score
        if distance < best_score:
            best_score = distance
            best = a[0]
    return best
