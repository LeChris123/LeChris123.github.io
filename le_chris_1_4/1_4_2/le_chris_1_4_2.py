# -*- coding: utf-8 -*-
'''
JDoe_JSmith_1_4_2: Read and show an image.
'''
import matplotlib.pyplot as plt
import os.path
import numpy as np # “as” lets us use standard abbreviations
   
'''Read the image data'''

directory = os.path.dirname(os.path.abspath(__file__)) 
filename = os.path.join(directory, 'cat.gif')
img = plt.imread(filename)
fig, ax = plt.subplots(1, 3)
ax[0].imshow(img)
ax[1].imshow(img, interpolation='none') # Override default
ax[2].imshow(img)
ax[0].set_xlim(10, 16)
ax[0].set_ylim(60, 85)
ax[1].set_xlim(15, 25)
ax[1].set_ylim(15, 30)
ax[2].set_xlim(25, 35)
ax[2].set_ylim(75, 90)
fig.show()
