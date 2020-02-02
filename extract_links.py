import fileinput
import urllib.request

from bs4 import BeautifulSoup

resp = urllib.request.urlopen("http://www.sciencekids.co.nz/pictures/flags.html")
soup = BeautifulSoup(
    resp, from_encoding=resp.info().get_param("charset"), features="lxml"
)

# print(soup.prettify())


def extract_links(out_file):

    fout = open(out_file, "w")

    for link in soup.find_all("a", href=True):
        fout.write(link["href"] + "\n")

    fout.close


def remove_duplicate_lines(in_file, out_file):

    lines_seen = set()  # holds lines already seen
    fin = open(in_file, "r")
    fout = open(out_file, "w")

    for line in fin:
        if line not in lines_seen:  # not a duplicate
            fout.write(line)
            lines_seen.add(line)

    fout.close()
    fin.close


def extract_country_names(in_file, out_file):

    fin = open(in_file, "rt")
    fout = open(out_file, "wt")

    for line in fin:
        line = line.replace("flags/", "")
        fout.write(line.replace(".html", ""))

    fin.close()
    fout.close()


extract_links("./resources/countries.txt")
remove_duplicate_lines("./resources/countries.txt", "./resources/flag_links.txt")
extract_country_names("./resources/flag_links.txt", "./resources/country_names.txt")
