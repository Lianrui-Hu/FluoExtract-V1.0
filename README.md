# Color Count in Images
This script is designed to count the number of yellow and blue pixels in an image and display the ratio of yellow to blue pixels. The script uses OpenCV and numpy for image processing.

# Prerequisites
* Python 3.x
* OpenCV
* numpy

# Installation
Before running the script, make sure you have OpenCV and numpy installed. You can install these packages using pip:
'''
pip install opencv-python numpy
'''

# Usage
Save the script as color_count.py.
Replace "Path-to-Picturefiles" with the actual path to your directory containing the images.
Run the script:

python color_count.py

# Path to the directory containing the images
path = "Path-to-Picturefiles"

# Key Functions
color_count(image_name): This function processes an image to count the yellow and blue pixels, calculates their ratio, and displays the original and thresholded images.

# Notes
Ensure the images are located in the specified directory path.
The script will process each image file in the specified directory and display the results.
# Author
[Your Name] - [Your Contact Information]

# License
This project is licensed under the MIT License - see the LICENSE.md file for details.
