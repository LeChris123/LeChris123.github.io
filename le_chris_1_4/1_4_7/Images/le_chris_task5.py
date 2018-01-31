from PIL import Image, ImageFilter
import numpy as np  
import matplotlib.pyplot as plt
import os.path
directory = os.path.dirname(os.path.abspath(__file__)) 
file = os.path.join(directory, 'salt.jpg')
img = plt.imread(file)
fig, ax = plt.subplots(1, 1)
height = len(img)
width = len(img[0])
print ('w = ',width)
print ('h = ',height)
def artsy(im):
    for row in range(height):
        for col in range(width):
            if (sum(img[row][col]))%5 == 2:
                im[row][col] = [row, 150, 255,]  
artsy(img)

ax.imshow(img, interpolation='none')
fig.show('salt.jpg')
file.save('salt.jpg')