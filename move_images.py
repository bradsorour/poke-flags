import os

from shutil import copyfile, rmtree

RESOURCES_ROOT = "./resources/"
images = ["pokemon", "flags"]
colours = ["green", "blue", "yellow", "red", "white", "black", "no_colours"]


def copy_images_to_colour_folder(in_file, colour, image):

    if os.path.exists(RESOURCES_ROOT + image + "/" + colour):
        rmtree(RESOURCES_ROOT + image + "/" + colour)

    if not os.path.exists(RESOURCES_ROOT + image + "/" + colour):
        os.makedirs(RESOURCES_ROOT + image + "/" + colour)

    if colour != "no_colours":
        fin = open(in_file, "rt")
    else:
        fin = open("./resources/data/no_colours.txt", "rt")

    for line in fin:
        image_file = "./resources/" + image + "_all/" + line.strip("\n")

        if not os.path.exists(image_file):
            print("Source file does not exist: {}".format(image_file))
            continue
        else:
            copyfile(
                image_file,
                RESOURCES_ROOT + image + "/" + colour + "/" + line.strip("\n"),
            )
            print("Copying... " + image_file)

    fin.close()


for colour in colours:

    # Run remove_duplicate_lines in extract_links.py first
    for image in images:
        copy_images_to_colour_folder(
            RESOURCES_ROOT + "data/" + image + "_" + colour + "_set.txt", colour, image
        )

