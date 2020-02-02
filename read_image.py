import os
from collections import Counter

import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.color import deltaE_cie76, rgb2lab
from sklearn.cluster import KMeans

ordered_colors = []
rgb_colors = []

IMAGE_DIRECTORY = "./resources/images/"
IMAGE_FILE = "sample_image.jpg"
image = cv2.imread(IMAGE_DIRECTORY + IMAGE_FILE)
# print("The type of this input is {}".format(type(image)))
# print("Shape: {}".format(image.shape))
# plt.imshow(image)
# plt.show()

# To move from BGR color space to RGB, we use the method cv2.COLOR_BGR2RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# plt.imshow(image)
# plt.show()

# In some situations, we might want to have black and white images.
# In such cases, we can express images as Gray.
# We now use the conversion space as cv2.COLOR_BGR2GRAY and show the
# output with the colormap as gray.
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# plt.imshow(gray_image, cmap='gray')
# plt.show()

# We can also resize the image to a given dimension.
# We use the method resize provided by cv2. The first argument is
# the image we want to resize, and the second argument is the width
# and height defined within parentheses.
resized_image = cv2.resize(image, (1200, 600))
# resized_image = cv2.resize(image, (215, 215))
# plt.imshow(resized_image)
# plt.show()

# Identifying the colors from an image and displaying the top colors as a pie chart.
# First define a function that will convert RGB to hex so that we can use them as labels for our pie chart.
# On reading the color which is in RGB space, we return a string. {:02x} simply displays the hex value for the respective color


def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))


# Define a method that will help get an image into Python in the RGB space.
def get_image(image_path):
    image = cv2.imread(image_path)

    if np.shape(image) == ():
        print("FAIL")

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image


def get_colors(image, number_of_colors, show_chart):

    # Resize the image to the size 600 x 400. It is not required to resize it to a smaller size but
    # we do so to lessen the pixels which’ll reduce the time needed to extract the colors from the image.
    # KMeans expects the input to be of two dimensions, so we use Numpy’s reshape function to reshape the image data.
    modified_image = cv2.resize(image, (600, 400), interpolation=cv2.INTER_AREA)
    modified_image = modified_image.reshape(
        modified_image.shape[0] * modified_image.shape[1], 3
    )
    # plt.imshow(modified_image)
    # plt.show()

    # KMeans algorithm creates clusters based on the supplied count of clusters.
    # In our case, it will form clusters of colors and these clusters will be our top colors.
    # We then fit and predict on the same image to extract the prediction into the variable labels.
    clf = KMeans(n_clusters=number_of_colors)
    labels = clf.fit_predict(modified_image)

    # We use Counter to get count of all labels. To find the colors, we use clf.cluster_centers_.
    # The ordered_colors iterates over the keys present in count, and then divides each value by 255.
    # We could have directly divided each value by 255 but that would have disrupted the order.
    counts = Counter(labels)
    center_colors = clf.cluster_centers_

    # We get ordered colors by iterating through the keys.
    # Next, we get the hex and rgb colors. As we divided each color by 255 before, we now multiply it by
    # 255 again while finding the colors. If show_chart is True, we plot a pie chart with each pie chart
    # portion defined using count.values(), labels as hex_colors and colors as ordered_colors.
    # We finally return the rgb_colors which we’ll use at a later stage.
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
    rgb_colors = [ordered_colors[i] for i in counts.keys()]

    print("\nRGB")
    for i in rgb_colors:
        print(i)

    print("\nORDERED")
    for i in ordered_colors:
        print(i)

    print("\nHEX")
    for i in hex_colors:
        print(i)

    if show_chart:
        plt.figure(figsize=(8, 6))
        plt.pie(counts.values(), labels=hex_colors, colors=hex_colors)
        plt.show()

    return rgb_colors


get_colors(get_image(IMAGE_DIRECTORY + IMAGE_FILE), 8, False)

