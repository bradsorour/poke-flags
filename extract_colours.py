import os

RESOURCES_ROOT = "./resources/"
colours = ["green", "blue", "yellow", "red", "white", "black"]
images = ["pokemon", "flags"]
colour_dict_flags = {}
colour_dict_pokemon = {}
missing_colours = []

# get filenames from the image directory
def get_image_filenames(image_dir, image_type):
    image_list = os.listdir(image_dir)
    return add_image_colours_to_dict(image_list, image_type)


# check if image present in colour folders and add to image/colour dictionary
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

        # create a list of images that don't have any colours
        # adjust RGB and threshold and run filter_images.py
        # again on these images to improve accuracy
        if len(image_colours) == 0:
            missing_colours.append(image_file)

    if image_type == images[0]:
        colour_dict_pokemon = colour_dict.copy()
        return colour_dict_pokemon
    else:
        colour_dict_flags = colour_dict.copy()
        return colour_dict_flags


pokemon_dict = get_image_filenames(RESOURCES_ROOT + images[0] + "_all", images[0])
flag_dict = get_image_filenames(RESOURCES_ROOT + images[1] + "_all", images[1])


def get_images_that_have_no_colours():

    fout = open("./resources/data/no_colours.txt", "w")

    print("No colours for images:\n")
    for image in missing_colours:
        fout.write(image + "\n")
        print("- " + image)

    fout.close


def get_pokemons_for_flag():
    for flag_key in flag_dict:
        print(flag_key + " " + str(flag_dict.get(flag_key)))

        for pokemon_key in pokemon_dict:
            if flag_dict.get(flag_key) == pokemon_dict.get(pokemon_key):
                print("- " + pokemon_key)


get_pokemons_for_flag()

print("\n============================\n")

get_images_that_have_no_colours()
