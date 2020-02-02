import os

import matplotlib.pyplot as plt
import numpy as np
from skimage.color import deltaE_cie76, rgb2lab

from read_image import get_colors, get_image

# Supply the RGB values for the colors Green, Blue and Yellow and let our system filter the images.
IMAGE_DIRECTORY = "./resources/flags/"
COLORS = {"GREEN": [0, 128, 0], "BLUE": [0, 0, 128], "YELLOW": [255, 255, 0]}
images = []
filenames = []

for file in os.listdir(IMAGE_DIRECTORY):
    if not file.startswith("."):
        images.append(get_image(file, os.path.join(IMAGE_DIRECTORY, file)))
        filenames.append(file)

# A method to filter all images that match the selected color.
# First extract the image colors using our previously defined method get_colors in RGB format.
# Use the method rgb2lab to convert the selected color to a format we can compare.
# The for loop simply iterates over all the colors retrieved from the image.

# For each color, the loop changes it to lab, finds the delta (difference) between the
# selected color and the color in iteration and if the delta is less than the threshold, the image
# is selected as matching with the color. We need to calculate the delta and compare it to the
# threshold because for each color there are many shades and we cannot always exactly match the
# selected color with the colors in the image.


def match_image_by_color(filename, image, color, threshold=60, number_of_colors=10):

    flag_colours_dict = {}
    image_colors = get_colors(
        flag_colours_dict, filename, image, number_of_colors, False
    )
    selected_color = rgb2lab(np.uint8(np.asarray([[color]])))

    select_image = False
    for i in range(number_of_colors):
        curr_color = rgb2lab(np.uint8(np.asarray([[image_colors[i]]])))
        diff = deltaE_cie76(selected_color, curr_color)
        if diff < threshold:
            select_image = True

    return select_image


# A function that iterates over all images, calls the above function to filter them
# based on color and displays them on the screen using imshow.
def show_selected_images(filenames, images, color, threshold, colors_to_match):
    index = 1

    for i in range(len(images)):
        selected = match_image_by_color(
            filenames[i], images[i], color, threshold, colors_to_match
        )
        if selected:
            plt.subplot(1, 5, index)
            plt.imshow(images[i])
            index += 1
            plt.show()


# Filter the results. Variable 'selected_color' can be any of COLORS['GREEN'], COLORS['BLUE'] or COLORS['YELLOW'].
# We set the threshold value to be 60 and total colors to be extracted from image to be 8.
plt.figure(figsize=(20, 10))
show_selected_images(filenames, images, COLORS["YELLOW"], 40, 4)
