#!/usr/bin/env python
# coding: utf-8

# In[20]:


from PIL import Image
import numpy as np


# In[40]:


Lancome_database = []
def shade_value(filename):
    if ".png" in filename:
        filename = filename.split(".png")[0]
    shade = Image.open(filename + ".png").convert('RGB')
    width, height = shade.size
    shade_values_red = []
    shade_values_green = []
    shade_values_blue = []
    for i in range(width):
        for j in range(height):
            shade_pixel = shade.getpixel((i,j))
            if shade_pixel[0] != 255:
                if shade_pixel[1] != 255:
                    if shade_pixel[2] != 255:
                        shade_values_red.append(shade_pixel[0])
                        shade_values_green.append(shade_pixel[1])
                        shade_values_blue.append(shade_pixel[2])
    shade_number = (int(np.mean(shade_values_red)), int(np.mean(shade_values_green)), int(np.mean(shade_values_blue)))
    return shade_number
def database(filename):
    if ".png" in filename:
        filename = filename.split(".png")[0]
    shade = shade_value(filename)
    database_entry = (filename, shade)
    return database_entry


# In[43]:


Love = database("4.png")
print(Love)


# In[ ]:




