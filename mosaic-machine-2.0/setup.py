# go through each image in library
# add to txt file for color matching
# sort so searching is easy using binary search

import helper
import os
import cv2 as cv

# make sure to have text file and images in same directory
path_to_library = "/Users/nemo/unsplash"
directory = os.fsencode(path_to_library)

# using append mode to add new lines
f = open(path_to_library + "/values.txt", 'a')

# go through every file in unsplash that is an image
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"): # or whatever file type
        img = cv.imread(path_to_library + "/" + filename)
        # remove the non number characters from the colour
        color = str(helper.calculateColour(img))
        color = color.replace('[', '')
        color = color.replace(',', '')
        color = color.replace(']', '')
        f.write(filename)
        f.write(" ")
        f.write(color)
        f.write('\n')

f.close()