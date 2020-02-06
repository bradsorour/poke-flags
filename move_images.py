import os

from shutil import copyfile, rmtree

RESOURCES_ROOT = "./resources/"
# FOLDER_COLOUR = "red"
IMAGE_TYPE = "pokemon"
colours = ["green", "blue", "yellow", "red", "white", "black"]


def copy_images_to_colour_folder(in_file, colour):

    if os.path.exists(RESOURCES_ROOT + IMAGE_TYPE + "/" + colour):
        rmtree(RESOURCES_ROOT + IMAGE_TYPE + "/" + colour)

    if not os.path.exists(RESOURCES_ROOT + IMAGE_TYPE + "/" + colour):
        os.makedirs(RESOURCES_ROOT + IMAGE_TYPE + "/" + colour)

    fin = open(in_file, "rt")

    for line in fin:

        # for pokemon images
        image_file = RESOURCES_ROOT + IMAGE_TYPE + "_all/jpg/" + line.strip("\n")
        # print("image file: " + image_file)
        # for flag images
        # image_file = "./resources/" + IMAGE_TYPE + "_all/" + line.strip("\n")

        if not os.path.exists(image_file):
            # raise ValueError("Source file does not exist: {}".format(image_file))
            print("Source file does not exist: {}".format(image_file))
            continue

        else:
            # copied_file = RESOURCES_ROOT + IMAGE_TYPE + "/" + colour + "/" + line.strip("\n")
            copyfile(
                image_file,
                RESOURCES_ROOT + IMAGE_TYPE + "/" + colour + "/" + line.strip("\n"),
            )

            print("Copying... " + image_file)

    fin.close()


for colour in colours:

    # For pokemon images
    # Run remove_duplicate_lines in extract_links.py first
    copy_images_to_colour_folder(
        RESOURCES_ROOT + "data/" + IMAGE_TYPE + "_" + colour + "_set.txt",
        colour
        # RESOURCES_ROOT + IMAGE_TYPE + "/" + FOLDER_COLOUR + "/",
    )

# For flag images
# copy_images_to_colour_folder(
#     RESOURCES_ROOT + IMAGE_TYPE + "_" + FOLDER_COLOUR + ".txt",
#     RESOURCES_ROOT + IMAGE_TYPE + "/" + FOLDER_COLOUR + "/",
# )

