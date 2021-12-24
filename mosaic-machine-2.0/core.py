import numpy as np
import cv2 as cv
import sys
import helper

# Change these accordingly
original_path = 'lena.png'  # path to original image
default_export = "saved_final.png"  # filename of exported image
path_to_library = "/Users/nemo/unsplash"  # path to library of images 

# Take command line arguments as exported filename
if (len(sys.argv)):
    saved_filename = str(sys.argv[0])
else:
    saved_filename = default_export

img = cv.imread(original_path)

# Get size and dimensions of image
x = img.shape[1]
y = img.shape[0]


# Representing a grid of squares over an image

# First, find all common divisors of the x and y
# To do this first find the greatest common divisor
# Then find the divisors of the GCD to find all divisors
factors = [np.gcd(x, y)]

# Each of these factors is a possible side length of the square in the grid
# for a 10x10 image, the divisors would be 1, 2, 5 meaning the 10x10 image
# could be split up into a grid of 1x1 squares (pixels), 2x2 squares, and
# 5x5 squares (4 of them) and obviously a 10x10 square

# Next, find all divisors up to that GCD and add to the list
for i in range(factors[0]//2, 0, -1):
    if (factors[0] % i == 0):
        factors.append(i)

# Print out all the possible factors as percentages of the image size
for i in range(len(factors)):
    if (100//factors[i] == 0):
        print(i+1, ". ", "1/", factors[i], sep="")
    else:
        print(i+1, ". ", 100//factors[i], "%", sep="")

# Let the user choose the percentage
percent = input("What percentage? (use the corresponding position: 1, 2..)")
percent = factors[int(percent)-1]

# Now that we know the grid size,
# we must slice image into each square.
curr_y = -percent
curr_x = -percent

# Open the text file with dominant rgb values of each image in our library
# which is generated by setup.py
values = open(path_to_library + "/values.txt", 'r')
lines = values.readlines()

common_rgb_values = {}  # "123,45,67": "corresponding_tile.jpg"

# Add the square side length to y and x respectively to get each square
# OpenCV uses the top left of the image as 0,0
for i in range(y//percent):
    curr_y += percent
    curr_x = -percent
    print(i, "/", y//percent)
    for j in range(x//percent):
        curr_x += percent
        # Create a cropped square using the current constraints
        crop = img[curr_y:curr_y+percent, curr_x:curr_x+percent]
        # Calculate the dominant colour of our square in the grid
        color = helper.calculateColour(crop)
        # Check if our colour is already in our dictionary
        if str(color) in common_rgb_values:
            image_path = common_rgb_values[str(color)]
        else:
            # Go through each line in the text file
            # Find the closest colour and return the filename
            image_path = helper.searchLines(lines, color)
            common_rgb_values[str(color)] = image_path
        # Use the corresponding image (resize and place in that grid square)
        tile = cv.imread(path_to_library + "/" + image_path)
        tile = cv.resize(tile, (percent, percent))
        img[curr_y:curr_y+percent, curr_x:curr_x+percent] = tile

# Close the text file
values.close()

# Show the final image
cv.imshow("test", img)

# First ask if user would like to download
if (input("Would you like to download? (Y/n) ") == 'n'):
    pass
else:
    try:
        cv.imwrite(saved_filename, img)
    # if the command line argument is erroneous, use default filename to export
    except Exception:  
        saved_filename = default_export
        cv.imwrite(saved_filename, img)
cv.waitKey(0)
