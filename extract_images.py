import os
from urllib.parse import urljoin, urlparse

import requests

from bs4 import BeautifulSoup as bs
from tqdm import tqdm

# When you extract the URL of images from a web page, there are quite a lot of URLs
# that are relative, which means it does not contain the full absolute URL with the
# scheme. So we need a way to check whether a URL is absolute.
def is_absolute(url):
    return bool(urlparse(url).netloc)


# urlparse() function parses a URL into six components, we just need to see if the netloc (domain name) is there.
# There are URLs of some websites that put encoded data in the place of a URL, we need to skip those.
# This function that validates every URL passed.
def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


# The HTML content of the web page is in soup object, to extract all img tags in HTML, we need to use soup.find_all("img") method.
# Returns all image URLs of a webpage
def get_all_images(url):
    soup = bs(requests.get(url).content, "html.parser")
    # print(soup.prettify())
    urls = []
    for img in tqdm(soup.find_all("img"), "Extracting images"):
        img_url = img.attrs.get("src")

        if not img_url:
            # if img does not contain src attribute, just skip
            continue

        if not is_absolute(img_url):
            # if img has relative URL, make it absolute by joining
            img_url = urljoin(url, img_url)

        # remove URLs like '/hsts-pixel.gif?c=3.2.5'
        try:
            pos = img_url.index("?")
            img_url = img_url[:pos]
        except ValueError:
            pass

        # finally, if the url is valid
        if is_valid(img_url):
            urls.append(img_url)

    return urls


# Downloads a file given an URL and puts it in the folder `pathname`
def download(url, pathname):

    # if path doesn't exist, make that path dir
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
        
    # download the body of response by chunk, not immediately
    response = requests.get(url, stream=True)

    # get the total file size
    file_size = int(response.headers.get("Content-Length", 0))

    # get the file name
    filename = os.path.join(pathname, url.split("/")[-1])

    # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
    progress = tqdm(
        response.iter_content(1024),
        f"Downloading {filename}",
        total=file_size,
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
    )
    with open(filename, "wb") as f:
        for data in progress:
            # write data read to the file
            f.write(data)
            # update the progress bar manually
            progress.update(len(data))


def main(url, path):
    # get all images
    imgs = get_all_images(url)
    for img in imgs:
        # for each img, download it
        download(img, path)


image_names = []

def load_image_file(filepath, uri):

    image_file = open(filepath, "r")
    string_uri = uri

    for image_name in image_file:
        image_name = image_name.strip('\n') 
        image_names.append(string_uri + image_name)

    image_file.close()


load_image_file("./resources/pokemon_names.txt", "https://pokemondb.net/pokedex/")

for image_name in image_names:
    main(image_name, "./resources/images/pokemon")



# pokemon_file = open("./resources/pokemon_names.txt", "r")
# string_uri = "https://pokemondb.net/pokedex/"
# pokemon_names = []

# for pokemon_name in pokemon_file:
#     pokemon_name = pokemon_name.strip('\n') 
#     pokemon_names.append(string_uri + pokemon_name)

# pokemon_file.close()

# for pokemon_name in pokemon_names:
#     main(pokemon_name, "./resources/images/pokemon")

