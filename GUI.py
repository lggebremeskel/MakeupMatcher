from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
import Makeupdatabasegenerator as mk

def openfilename():
    '''
    This function will intiniate a dialog box to open a PNG image. 
    '''
    filename = filedialog.askopenfilename(title ='"Image', filetypes = [("PNG files", "*.PNG")])
    return filename

def analyzer(picture):
    '''
    This takes in an image and converts it to a list with the RGB values.
    **Parameters**:
        picture: *str*
            This the name of the image you would like to convert to an RGB value
    **Returns**
        shade_number : *array*
            an array of the R,G and B values of the image inputted.
    '''
    shade = Image.open(picture).convert('RGB')
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

def close(brand,shade):
    '''
    This takes in the RGB value of an image and the database with the shade options for the desired make-ip brand and 
    matches the image shade to the closest shade in the database.
    **Parameters**:
        brand: *list of lists*
            This is a list with all the available shades of the brand
    **Returns**
        shade: *array*
            an array of the R,G and B values of the image inputted.
    '''
    return brand[min(range(len(brand)), key = lambda i: ((abs(brand[i][1][0] - shade[0])) + (abs(brand[i][1][1] - shade[1])) + (abs(brand[i][1][2] - shade[2]))))]

class user_inf(tk.Frame):
    def __init__(self, master):
        '''
    The user_inf class inherits the Tk.frame class from the tkinter module. It is a graphical user interface which 
    will allow the user to upload an image, see an example image if necessary and choose a make-up brand. It will 
    the ran a function to match the users image to the closest shade in the chosen brand.
        '''
        self.master = master
        self.widgets()
        self.view_img = None
        self.error_msg = None
        self.fenty_shade_result = None
        self.lancome_shade_result = None
        self.dior_shade_result = None

    def example_img(self):
        '''
        This opens the example image.
        '''
        Image.open('Example.JPG').show()
    def image_opener(self):
        '''
        This will open the image the user uploaded

        '''
        if self.view_img is not None:
            self.view_img.destroy()
        if self.error_msg is not None:
            self.error_msg.destroy()
        if self.fenty_shade_result is not None:
            self.fenty_shade_result.destroy()
        if self.dior_shade_result is not None:
            self.dior_shade_result.destroy()
        if self.lancome_shade_result is not None:
            self.lancome_shade_result.destroy()
        self.picture = openfilename()
        pic = Image.open(self.picture)
        pic = pic.resize((50, 50), Image.ANTIALIAS)
        pic = ImageTk.PhotoImage(pic)
        self.view_img = Label(self.master, image = pic)
        self.view_img.place(x = 450, y = 150)
        self.view_img.image = pic 

    def compare(self, picture, brand):
        '''
        This takes in the image provided by the user and uses the close function to 
        match the user's shade with a shade from the users chosen brand.
        **Parameters**:
            picture: *str*
                filename of the image the user provided 
            brand: *list*
                The database of the brand the user chose 
        **Returns**:
            The name of the shade that matches the users image 
        '''
        try:
            shade = analyzer(picture)
            if brand == 'Fenty':
                fenty_recommend = close(mk.Fenty_database,shade)
                fenty_shade = fenty_recommend[0]
                self.fenty_shade_result = Label(self.master,text = 'Your recommended Fenty shade is, ' + fenty_shade, fg = 'green')
                self.fenty_shade_result.place(x = 100, y = 300)
                return fenty_shade
            if brand == 'Lancome':
                lancome_recommend = close(mk.Lancome_database,shade)
                lancome_shade = lancome_recommend[0]
                self.lancome_shade_result = Label(self.master,text = 'Your recommended Lancome shade is, ' + lancome_shade, fg = 'blue')
                self.lancome_shade_result.place(x = 100, y = 350)
                return lancome_shade
            if brand == 'Dior':
                dior_recommend = close(mk.Dior_database,shade)
                dior_shade = dior_recommend[0]
                self.dior_shade_result = Label(self.master,text = 'Your recommended Dior shade is, ' + dior_shade, fg = 'brown')
                self.dior_shade_result.place(x = 100, y = 400)
                return dior_shade
        except AttributeError:
            self.error_msg = Label (self.master, text = 'Error: Please upload a .PNG image first.', fg = 'red' )
            self.error_msg.place(x = 285, y = 450)
        
    def widgets(self):
        '''
            This places the widgets for the class.
        '''
        self.welcome = Label(self.master,text = 'Welcome!', fg = 'black')
        self.welcome.place(x = 350, y = 50)
        self.upload_request = Label(self.master,text = 'Please upload a close up picture of your hand \nClick "Example Button" to see example image', fg = 'black')
        self.upload_request.place(x = 200, y = 100)
        self.exp_img = Button(self.master, text = 'Example' , fg = 'red', command = lambda: self.example_img())
        self.exp_img.place(x = 450, y = 110)
        self.up_img = Button(self.master, text = 'Upload Image' , command = lambda: self.image_opener())
        self.up_img.place(x = 340, y = 150)
        self.fenty = Button(self.master, text='Fenty', fg='blue', command = lambda: self.compare(self.picture, 'Fenty'))
        self.fenty.place(x = 200, y = 250)
        self.lancome = Button(self.master, text='Lancome', fg='blue', command = lambda: self.compare(self.picture, 'Lancome'))
        self.lancome.place(x = 350, y = 250)
        self.dior = Button(self.master, text='Dior', fg='blue', command = lambda: self.compare(self.picture,'Dior'))
        self.dior.place(x = 500, y = 250)
if __name__ == '__main__':
    mk.initialize_databases()
    root =Tk()
    root.title("Make-up Matcher")
    root.geometry("700x500")
    app = user_inf(master=root)
    root.mainloop()



