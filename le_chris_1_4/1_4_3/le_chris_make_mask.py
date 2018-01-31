import matplotlib.pyplot as plt
import numpy as np
import PIL

def make_mask(rows, columns, stripe_width):

    img = PIL.Image.new('RGBA', (columns, rows))
    image = np.array(img)
    for row in range(rows):
        for column in range(columns):
            if (row+column)/stripe_width % 3 == 0: 
                # Even stripe
                image[row][column] = [255, column, 0, 150] 
            elif (row+column)/stripe_width %3 == 1:
                image[row][column] = [25, column, 0, 100]
            else:
                # Odd stripe
                image[row][column] = [15, column, 235, 255] 
    return image
    
if __name__ == "__main__":
    image = make_mask(300,255,10)
    
    fig, ax = plt.subplots(1, 1)
    ax.imshow(image)
    fig.show()            
              
