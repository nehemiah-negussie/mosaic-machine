import helper
import os
import cv2 as cv

# Make sure to have text file and images in same directory
path_to_library = "/Users/nemo/unsplash"

directory = os.fsencode(path_to_library)

# Using append mode to add new lines
f = open(path_to_library + "/values.txt", 'a')

# Progress counter
progress = 1

# go through every file in unsplash that is an image
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    print(progress, "/", len(os.listdir(directory)))
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):  # or whatever file type
        img = cv.imread(path_to_library + "/" + filename)
        # Remove the non number characters from the colour
        color = str(helper.calculateColour(img))

        color = color.replace('[', '')
        color = color.replace('.', '')
        color = color.replace(']', '')
        # Write filename and colour with newline in file
        f.write(filename)
        f.write(" ")
        f.write(color)
        f.write('\n')
    progress += 1
f.close()
