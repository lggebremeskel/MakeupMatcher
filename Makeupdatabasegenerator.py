from PIL import Image
import numpy as np
import os

Lancome_database = [] 
Dior_database = []
Fenty_database = []
#global variables to store each available shade with their RGB values

def shade_value(filename):
    '''
    This takes in an image and converts it to a list with the RGB values.
    **Parameters**:
        filename: *str*
            This the name of the image you would like to convert to an RGB value
    **Returns**
        shade_number : *array*
            an array of the R,G and B values of the image inputted.
    '''
    shade = Image.open(filename).convert('RGB')
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
def directory_reader(folder_path,database):
    '''
    This takes in the directory of where the images representing each shade of the make-up brands are stored and converts them to 
    an array of the filename and the RGB value. 
    **Parameters**:
        folder_path: *str*
            A directory to where the folder with the foundation options is located.
        database: *list*
            A list to store the name and RGB of each shade for the foundation path.
    '''
    for i in os.listdir(folder_path):
        if i.endswith(".PNG"):
            shade = shade_value(folder_path + '\\' + i)
            shade_name = i.split(".PNG")[0]
            database_entry = (shade_name, shade)
            database.append(database_entry)  
def initialize_databases():
    '''
    This function initializes the creation of the global variables that store each shade for all three make-up types.
    '''
    current_directory = os.getcwd()
    directory_reader(current_directory + "\\Foundations\FENTY PRO FILTR SOFT MATTE",Fenty_database)
    directory_reader(current_directory + "\\Foundations\LANCOME TEINT IDOLE ULTRA 24H LONG WEAR FOUNDATION",Lancome_database)
    directory_reader(current_directory + "\\Foundations\DIOR FOREVER",Dior_database)


