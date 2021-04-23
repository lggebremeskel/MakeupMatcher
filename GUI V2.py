from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
import Makeupdatabasegenerator as MK

def openfilename():
    filename = filedialog.askopenfilename(title ='"Image')
    #add png only selection
    return filename

def analyzer(picture):
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
    return brand[min(range(len(brand)), key = lambda i: ((abs(brand[i][1][0] - shade[0])) + (abs(brand[i][1][1] - shade[1])) + (abs(brand[i][1][2] - shade[2]))))]

class user_inf2(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.widgets()
    def example_img(self):
        pic = Image.open('2.png')
        plt.imshow(pic)   
    def image_opener(self):
        self.picture = openfilename()
        pic = Image.open(self.picture)
        pic = pic.resize((50, 50), Image.ANTIALIAS)
        pic = ImageTk.PhotoImage(pic)
        self.view = Label(self.master, image = pic)
        self.view.place(x = 300, y = 150)
        self.view.image = pic 
    def compare(self, picture, brand):
        shade = analyzer(picture)
        if brand == 'Fenty':
            fenty_recommend = close(mk.Fenty_database,shade)
            fenty_shade = fenty_recommend[0]
            self.fenty_shade_result = Label(self.master,text = 'Your recommended shade is, ' + fenty_shade, fg = 'green')
            self.fenty_shade_result.place(x = 100, y = 300)
            return fenty_shade
        if brand == 'Lancome':
            lancome_recommend = close(mk.Lancome_database,shade)
            lancome_shade = lancome_recommend[0]
            return lancome_shade
        if brand == 'Dior':
            dior_recommend = close(mk.Dior_database,shade)
            dior_shade = dior_recommend[0]
            return dior_shade
    def widgets(self):
        self.welcome = Label(self.master,text = 'Welcome!', fg = 'black')
        self.welcome.place(x = 200, y = 50)
        self.upload_request = Label(self.master,text = 'Please upload a close up picture of your hand \nClick "Example Button" to see example image', fg = 'black')
        self.upload_request.place(x = 100, y = 100)
        self.exp_img = Button(self.master, text = 'Example' , fg = 'red', command = lambda: self.example_img())
        self.exp_img.place(x = 350, y = 110)
        self.up_img = Button(self.master, text = 'Upload Image' , command = lambda: self.image_opener())
        self.up_img.place(x = 200, y = 150)
        self.fenty = Button(self.master, text='Fenty', fg='blue', command = lambda: self.compare(self.picture, 'Fenty'))
        self.fenty.place(x = 100, y = 250)
        self.lancome = Button(self.master, text='Lancome', fg='blue', command = lambda: compare(self.picture, 'Lancome'))
        self.lancome.place(x = 150, y = 250)
        self.dior = Button(self.master, text='Dior', fg='blue', command = lambda: compare(self.picture,'Dior'))
        self.dior.place(x = 250, y = 250)
if __name__ == '__main__':
    mk.initialize_databases()
    root =Tk()
    root.title("Make-up Matcher")
    root.geometry("500x400")
    app = user_inf2(master=root)
    root.mainloop()



