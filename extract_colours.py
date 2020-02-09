import os

from shutil import copyfile, rmtree

from subprocess import call

RESOURCES_ROOT = "./resources/"
COPY_DIR = "flag_pokemons/"
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


def get_pokemons_for_all_flags():
    for flag_key in flag_dict:
        print(flag_key + " " + str(flag_dict.get(flag_key)))

        for pokemon_key in pokemon_dict:
            if flag_dict.get(flag_key) == pokemon_dict.get(pokemon_key):
                print("- " + pokemon_key)


def get_pokemons_for_flag(country_flag, copy_to_dir):

    print(country_flag + " colours: " + str(flag_dict.get(country_flag)))
    print("Matching Pokemons: ")

    if copy_to_dir:

        if os.path.exists(RESOURCES_ROOT + COPY_DIR):
            rmtree(RESOURCES_ROOT + COPY_DIR)

        if not os.path.exists(RESOURCES_ROOT + COPY_DIR):
            os.makedirs(RESOURCES_ROOT + COPY_DIR)

    for pokemon_key in pokemon_dict:
        if flag_dict.get(country_flag) == pokemon_dict.get(pokemon_key):
            print("- " + pokemon_key)

            if copy_to_dir:
                flag_image = "./resources/flags_all/" + country_flag
                copyfile(flag_image, RESOURCES_ROOT + COPY_DIR + country_flag)
                pokemon_image = "./resources/pokemon_all/" + str(pokemon_key)
                copyfile(pokemon_image, RESOURCES_ROOT + COPY_DIR + str(pokemon_key))

    print("Matching pokemons copied to " + RESOURCES_ROOT + COPY_DIR)

    targetDirectory = RESOURCES_ROOT + COPY_DIR
    call(["open", targetDirectory])


# get_pokemons_for_all_flags()

# get_images_that_have_no_colours()

# get_pokemons_for_flag("Vanuatu.jpg")
