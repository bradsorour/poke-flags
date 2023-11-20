import fileinput
import urllib.request

from bs4 import BeautifulSoup

url = "http://www.sciencekids.co.nz/pictures/flags.html"
colours = ["green", "blue", "yellow", "red", "white", "black"]
images = ["pokemon", "flags"]
count = 0


def scrape_website(url):

    resp = urllib.request.urlopen(url)
    soup = BeautifulSoup(
        resp, from_encoding=resp.info().get_param("charset"), features="lxml"
    )


def extract_links(out_file):

    fout = open(out_file, "w")

    for link in soup.find_all("a", href=True):
        fout.write(link["href"] + "\n")

    fout.close


def remove_duplicate_lines(in_file, out_file, change_file_extension):

    line_count = 0
    lines_seen = set()  # holds lines already seen
    fin = open(in_file, "r")
    fout = open(out_file, "w")

    for line in fin:
        line_count += 1
        if line not in lines_seen:  # not a duplicate
            if change_file_extension:
                line = line.replace(".png", ".jpg")

            fout.write(line)
            lines_seen.add(line)

    print(in_file + " line_count: " + str(line_count))
    count = line_count - len(lines_seen)
    print(in_file + "lines removed: " + str(count))

    fout.close()
    fin.close


def extract_country_names(in_file, out_file):

    fin = open(in_file, "rt")
    fout = open(out_file, "wt")

    for line in fin:
        fout.write(line.replace("flags/", ""))

    fin.close()
    fout.close()


def remove_duplicates_from_all_colour_files():

    for image_type in images:
        for colour in colours:

            in_file = "./resources/data/" + image_type + "_" + colour + ".txt"
            out_file = "./resources/data/" + image_type + "_" + colour + "_set.txt"

            remove_duplicate_lines(
                in_file, out_file, True,
            )


remove_duplicates_from_all_colour_files()

# extract_links("./resources/data/countries.txt")
# remove_duplicate_lines("./resources/data/countries.txt", "./resources/data/flag_links.txt")
# extract_country_names("./resources/data/flag_links.txt", "./resources/data/country_names.txt")
