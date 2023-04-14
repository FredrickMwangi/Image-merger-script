# Import necessary libraries
import numpy as np
from PIL import Image

# Define a list of image file names
list_im = ['img1.jpeg', 'img2.jpeg', 'img3.jpeg']

# Create a list of PIL Image objects by opening each image file in the list
imgs = [Image.open(i) for i in list_im]

# Find the smallest image size among the opened images using np.sum function
# np.sum is used to calculate the total number of pixels in an image
# The smallest image size is determined based on the sum of pixel counts
min_shape = sorted([(np.sum(i.size), i.size ) for i in imgs])[0][1]

# Resize each image in the list to match the smallest image size
# The resized images are horizontally stacked using np.hstack
imgs_comb = np.hstack([i.resize(min_shape) for i in imgs])

# Create a new PIL Image object from the horizontally stacked image array using Image.fromarray method
# Then save the horizontally stacked image as a new JPEG file using Image.save method
imgs_comb = Image.fromarray(imgs_comb)
imgs_comb.save('merged_image.jpeg')

# Resize each image in the list to match the smallest image size
# The resized images are vertically stacked using np.vstack
imgs_comb = np.vstack([i.resize(min_shape) for i in imgs])

# Create a new PIL Image object from the vertically stacked image array using Image.fromarray method
# Then save the vertically stacked image as a new JPEG file using Image.save method
imgs_comb = Image.fromarray(imgs_comb)
imgs_comb.save('vertical_image.jpeg')
