import os

import json

import matplotlib.pyplot as plt

from read_image import get_colors, get_image

# Supply the RGB values for the colors Green, Blue and Yellow and let our system filter the images.
IMAGE_DIRECTORY = "./resources/pokemon_all/jpg/"
COLORS = {"GREEN": [0, 128, 0], "BLUE": [0, 0, 128], "YELLOW": [255, 255, 0]}
images = []


def get_image_colours():
    flag_colours_dict = {}
    for file in os.listdir(IMAGE_DIRECTORY):
        if not file.startswith("."):
            print("\n\nFile: " + file)
            images.append(get_image(file, os.path.join(IMAGE_DIRECTORY, file)))
            get_colors(
                flag_colours_dict,
                file,
                get_image(file, IMAGE_DIRECTORY + file),
                4,
                False,
            )

    # save dictionary to json file
    json_file = json.dumps(flag_colours_dict)
    f = open("./resources/pokemon_colours.json", "w")
    f.write(json_file)
    f.close()
    # fout.close


# Show all the images in the folder
def show_images():
    plt.figure(figsize=(20, 10))
    for i in range(len(images)):
        plt.subplot(1, len(images), i + 1)
        plt.imshow(images[i])
        plt.show()


get_image_colours()
# show_images()
