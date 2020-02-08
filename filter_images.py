import os

import matplotlib.pyplot as plt
import numpy as np
from skimage.color import deltaE_cie76, rgb2lab

from read_image import get_colors, get_image

# Supply the RGB values for the colors Green, Blue and Yellow and let our system filter the images.
# IMAGE_DIRECTORY = "./resources/pokemon/png/"
IMAGE_DIRECTORY = "./resources/pokemon_all/"
# IMAGE_DIRECTORY = "./resources/pokemon/no_colours/"
# IMAGE_DIRECTORY = "./resources/flags_all/"
POKEMON_PLOTS = 910
FLAG_PLOTS = 205

COLORS_FLAGS = {
    "GREEN": [0, 128, 0],
    "BLUE": [0, 0, 128],
    "YELLOW": [255, 255, 0],
    "RED": [128, 0, 0],
    "WHITE": [255, 255, 255],
    "BLACK": [0, 0, 0],
}

COLORS_POKEMON = {
    "GREEN": [0, 128, 0],
    "BLUE": [0, 128, 255],
    "YELLOW": [255, 255, 0],
    "RED": [128, 0, 0],
    "WHITE": [255, 255, 255],
    "BLACK": [0, 0, 0],
}
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
            fout.write(filename + "\n")
            print(">> " + filename)

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
            plt.subplot(1, POKEMON_PLOTS, index)
            index += 1


# Filter the results. Variable 'selected_color' can be any of COLORS['GREEN'], COLORS['BLUE'] or COLORS['YELLOW'].
# We set the threshold value to be 60 and total colors to be extracted from image to be 8.
plt.figure(figsize=(20, 10))

# 40, 4 Done
# fout = open("./resources/data/flags_yellow.txt", "w")
# print("** COLOUR YELLOW")
# show_selected_images(filenames, images, COLORS_FLAGS["YELLOW"], 40, 8)
# fout.close

# 40,4 Done
# fout = open("./resources/data/flags_green.txt", "w")
# print("** COLOUR GREEN")
# show_selected_images(filenames, images, COLORS_FLAGS["GREEN"], 40, 4)
# fout.close

# 64, 4 Done
# fout = open("./resources/data/flags_blue.txt", "w")
# print("** COLOUR BLUE")
# show_selected_images(filenames, images, COLORS_FLAGS["BLUE"], 65, 4)
# fout.close

# 40, 2 Done
# fout = open("./resources/data/flags_red.txt", "w")
# print("** COLOUR RED")
# show_selected_images(filenames, images, COLORS_FLAGS["RED"], 40, 2)
# fout.close

# 40, 2 Done
# fout = open("./resources/data/flags_white.txt", "w")
# print("** COLOUR WHITE")
# show_selected_images(filenames, images, COLORS_FLAGS["WHITE"], 40, 2)
# fout.close

# 35, 3 Done
# fout = open("./resources/data/flags_black.txt", "w")
# print("** COLOUR BLACK")
# show_selected_images(filenames, images, COLORS_FLAGS["BLACK"], 35, 3)
# fout.close

# 60, 10
fout = open("./resources/data/pokemon_yellow.txt", "w")
print("** COLOUR YELLOW")
show_selected_images(filenames, images, COLORS_POKEMON["YELLOW"], 80, 10)
fout.close

# fout = open("./resources/data/pokemon_green.txt", "w")
# print("** COLOUR GREEN")
# show_selected_images(filenames, images, COLORS_POKEMON["GREEN"], 57, 7)
# fout.close

# 70,7
# fout = open("./resources/data/pokemon_blue.txt", "w")
# print("** COLOUR BLUE")
# show_selected_images(filenames, images, COLORS_POKEMON["BLUE"], 53, 7)
# fout.close

# fout = open("./resources/data/pokemon_red.txt", "w")
# print("** COLOUR RED")
# show_selected_images(filenames, images, COLORS_POKEMON["RED"], 45, 7)
# fout.close

# # 20, 2
# fout = open("./resources/data/pokemon_black.txt", "w")
# print("** COLOUR BLACK")
# show_selected_images(filenames, images, COLORS_POKEMON["BLACK"], 20, 4)
# fout.close

# fout = open("./resources/data/pokemon_white.txt", "w")
# print("** COLOUR WHITE")
# show_selected_images(filenames, images, COLORS_POKEMON["WHITE"], 40, 2)
# fout.close

# 80, 10 Done
# fout = open("./resources/data/no_colours.txt", "w")
# print("** COLOUR YELLOW")
# show_selected_images(filenames, images, COLORS_POKEMON["YELLOW"], 80, 10)
# fout.close
