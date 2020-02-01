import requests
from bs4 import BeautifulSoup

# Set headers
# A lot of sites have precautions in place to fend off scrapers from accessing their data.
# The first thing we can do to get around this is spoofing the headers we send along with
# our requests to make it look like we're a legitimate browser:
headers = requests.utils.default_headers()
headers.update(
    {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

url = "https://en.wikipedia.org/wiki/List_of_Pok%C3%A9mon"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')
print(soup.prettify())
