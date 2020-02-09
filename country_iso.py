import csv
import os

from extract_colours import get_pokemons_for_flag

iso_dict = {}
image_dict = {}


def extract_country_iso_code(in_file, out_file):

    with open(in_file, "r") as csvinput:
        with open(out_file, "w") as csvoutput:
            writer = csv.writer(csvoutput, lineterminator="\n")
            reader = csv.reader(csvinput, skipinitialspace=False)
            all = []

            print("\n")

            for row in reader:
                iso_dict[row[0]] = row[1]
                row.append(row[1] + ".jpg")
                all.append(row)
                print(row[0] + " | " + row[1])

            writer.writerows(all)


def get_all_country_images_from_iso_codes(in_file):

    with open(in_file, "r") as csvinput:
        reader = csv.reader(csvinput)

        for row in reader:
            image_filename = row[2]
            image_file = "./resources/flags_all/" + image_filename
            image_dict[row[0]] = image_filename

            # if not os.path.exists(image_file):
            #     print(image_filename + " (** missing)")


extract_country_iso_code(
    "./resources/data/country_iso_codes.csv", "./resources/data/country_iso_images.csv"
)

get_all_country_images_from_iso_codes(
    "./resources/data/country_iso_images_formatted.csv"
)

iso_code_input = input("\nEnter country ISO code: ")
print(
    "You entered "
    + iso_code_input
    + ", country is "
    + str(iso_dict.get(iso_code_input) + " (" + image_dict.get(iso_code_input) + ")")
)

get_pokemons_for_flag(image_dict.get(iso_code_input), True)

