import os
from PIL import Image, ImageDraw

# Set the path to the directory containing the images
path = "images/"

# Get a list of all the image files in the directory
files = [f for f in os.listdir(path) if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.jpeg')]

# Starting number for the images
start_number = 1

# The number of digits in the zero-padded numbering format
num_digits = 4

# Iterate through the image files
for file in files:
    # Open the image
    img = Image.open(os.path.join(path, file))
    
    # Create an ImageDraw object
    draw = ImageDraw.Draw(img)


    # Position of the text
    position = (10, 10)

    t1 = 'im_'
    # The text to be added to the image
    text = t1 + str(start_number).zfill(num_digits)

    # Add the text to the image
    draw.text(position, text, fill=(255, 255, 255))

    # Save the image with the added text
    img.save(os.path.join(path, text +file))

    # increment the starting number
    start_number += 1

print("Images saved!")
