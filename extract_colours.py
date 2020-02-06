import os

RESOURCES_ROOT = "./resources/"
colours = ["green", "blue", "yellow", "red", "white", "black"]
images = ["pokemon", "flags"]
colour_dict_flags = {}
colour_dict_pokemon = {}

# get filenames from the image directory
def get_image_filenames(image_dir, image_type):
    image_list = os.listdir(image_dir)
    return add_image_colours_to_dict(image_list, image_type)


# check if image present in colour folders and add to image colour dictionary
def add_image_colours_to_dict(image_list, image_type):

    colour_dict = {}

    for image_file in image_list:
        image_colours = []
        for colour in colours:
            colour_dir = (
                RESOURCES_ROOT + "/data/" + image_type + "_" + colour + "_set.txt"
            )

            with open(colour_dir) as f:
                if image_file in f.read():
                    image_colours.append(colour)

            colour_dict[image_file] = image_colours

    if image_type == images[0]:
        colour_dict_pokemon = colour_dict.copy()
        return colour_dict_pokemon
    else:
        colour_dict_flags = colour_dict.copy()
        return colour_dict_flags


pokemon_dict = get_image_filenames(RESOURCES_ROOT + images[0] + "_all", images[0])
flag_dict = get_image_filenames(RESOURCES_ROOT + images[1] + "_all", images[1])

print(pokemon_dict.items())
print("===================")
print(flag_dict.items())
