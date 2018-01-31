from PIL import Image, ImageFilter
import os

image1 = Image.open('highland.JPG')
image1.convert(mode = 'L').save('highland.JPG')