# mosaic-machine!

mosaic-machine is the project which takes an image and creates a photomosaic using images from a library (tiles) to recreate the image. 


<img src="https://raw.githubusercontent.com/nehemiah-negussie/mosaic-machine/main/example/mona_mosaic.png" alt="drawing" width="400"/>

A large library of images will allow for more accurate results because of a larger sample size to match each pixel colour.

### Dominant vs Average colour
An issue that was ran into when calculating the overall colour of an image was what metric to use.  A natural response would be to use the average values of each pixels RGB value, which yields not so accurate results, such as the image below.

![](https://raw.githubusercontent.com/AdamSpannbauer/iphone_app_icon/master/readme/dom_color_k_1.jpg)
[Example of average colour, Adam Spannbauer](https://adamspannbauer.github.io/2018/03/02/app-icon-dominant-colors/)

*Using average colour*

![](https://raw.githubusercontent.com/nehemiah-negussie/mosaic-machine/main/example/lena.png) <img src="https://raw.githubusercontent.com/nehemiah-negussie/mosaic-machine/main/example/Screen%20Shot%202021-12-17%20at%2010.46.41%20PM.png" alt="drawing" width="220"/>

Another approach would be to use the most **dominant** colour in an image. This uses a simple clustering algorithm called K-means clustering to find clusters in an image and use the colour palette to choose the most common cluster.

*Using most dominant colour*

||![](https://raw.githubusercontent.com/nehemiah-negussie/mosaic-machine/main/example/lena.png) <img src="https://raw.githubusercontent.com/nehemiah-negussie/mosaic-machine/main/example/saved_final2.png" alt="drawing" width="220"/>
    
## Libraries, Languages and Tools
- Python
- OpenCV
- NumPy
- SciPy
- Pillow
- pip

**Optional:**
- NodeJS
- bulksplash
# Installation
*First*, clone the repository:
`git clone https://github.com/nehemiah-negussie/mosaic-machine.git	`

*Second*, install all libraries, languages and tools shown above.

*Third*, edit the `core.py` and `setup.py` file to your specific path to the library  and image paths.

*Fourth*, run the `setup.py` file using `python3 setup.py` to create a values.txt file that will be vital in the running of the program.

*Fifth*, go to the Usage section to run!
##### *Optional:* Library download using bulksplash
If you want to have a large library I recommend using the [bulksplash](https://github.com/MehediH/Bulksplash) tool.
You should export the artists to a JSON file so you can credit them, according to Unsplash's TOS.
# Usage

`python3 core.py [output file]`
Sample:
`python3 core.py awesome_landscape_mosaic.png`

The program will run and ask you what percentage of the original image to choose. A lower percentage will run significantly faster than higher percentages but will be more granular.

After the program is finished running, it will ask if the user would like to download the image then show the image finally.



## License

GNU GENERAL PUBLIC LICENSE
## Acknowledgements

All Unsplash artists that are used in my library are credited in the `bulksplash-credits.json` file.

