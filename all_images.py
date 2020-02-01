import os

import matplotlib.pyplot as plt

from read_image import get_image

# Supply the RGB values for the colors Green, Blue and Yellow and let our system filter the images.
IMAGE_DIRECTORY = "./resources/images/"
COLORS = {"GREEN": [0, 128, 0], "BLUE": [0, 0, 128], "YELLOW": [255, 255, 0]}
images = []

for file in os.listdir(IMAGE_DIRECTORY):
    if not file.startswith("."):
        print('==>> ' + file)
        images.append(get_image(os.path.join(IMAGE_DIRECTORY, file)))


# Show all the images in the folder
plt.figure(figsize=(20, 10))
for i in range(len(images)):
    plt.subplot(1, len(images), i + 1)
    plt.imshow(images[i])
    plt.show()
