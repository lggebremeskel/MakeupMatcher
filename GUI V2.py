#!/usr/bin/env python
# coding: utf-8

# In[113]:


from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog


# In[15]:


def openfilename():
    filename = filedialog.askopenfilename(title ='"okay')
    return filename
def analyzer():
    shade = Image.open(picture + ".png").convert('RGB')
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
   # def compare(shade_number,)


# In[20]:


def Gui():
    gui =tk.Tk()
    gui.title("Make-up Matcher")
    app = user_in(master=gui)
    gui.mainloop()


# In[17]:


def compare(Fenty):
    if Fenty == 'Fenty' or 'Lancome' or 'Dior':
        print("Made it")


# In[114]:


class user_in(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.welcome()
        self.example_img()
        self.upload_img()
        self.makeup_choice
        
    def welcome(self):
        print('Welcome')
        print('Please upload a close up picture of your hand as shown in the picture below')
    def example_img(self):
        return Image.open('2.png')
    def image_opener(self):
        picture = openfilename()
        if ".png" in picture:
            picture = picture.split(".png")[0]
        pic = Image.open(picture)
        pic = Image.resize((150, 150), Image.ANTIALIAS)
        pic = ImageTk.PhotoImage(pic)
        view = Label(root, image = pic)
        view.image = pic
        pic.grid()
    def upload_img(self):
        self.up_img = tk.Button(self, text = 'Upload Image' , command = self.image_opener)
    def makeup_choice(self):
        self.fenty = tk.Button(self, text='Fenty', fg='blue', command = self.compare('Fenty'))
        self.fenty.pack(side='left')
        self.lancome = tk.Button(self, text='Lancome', fg='blue', command = self.compare('Lancome'))
        self.fenty.pack(side='left')
        self.dior = tk.Button(self, text='Dior', fg='blue', command = self.compare('Dior'))
        self.fenty.pack(side='left')
    


# In[115]:


if __name__ == '__main__':
    root =tk.Tk()
    root.title("Make-up Matcher")
    app = user_in(master=root)
    root.mainloop()


# In[127]:


class user_inf(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.widgets()
    def example_img():
        return Image.open('2.png')
    def image_opener(self):
        picture = openfilename()
        if ".png" in picture:
            picture = picture.split(".png")[0]
        pic = Image.open(picture)
        pic = Image.resize((100, 100), Image.ANTIALIAS)
        pic = ImageTk.PhotoImage(pic)
        view = Label(self, image = pic)
        view.image = pic
        pic.grid()
    def compare(F):
        if F == 'Fenty' or 'Lancome' or 'Dior':
            print("Made it")   
    def widgets(self):
        self.welcome = Label(self,text = 'Welcome', fg = 'black')
        self.welcome.pack(side='top')
        self.upload_request = Label(self,text = 'Please upload a close up picture of your hand, Click "Example Button" to see example image', fg = 'black')
        self.upload_request.pack(side='top')
        self.exp_img = Button(self, text = 'Example' , command = Image.open('2.png'))
        self.exp_img.pack(side='top')
        self.up_img = Button(self, text = 'Upload Image' , command = self.image_opener)
        self.up_img.pack(side='top')
        self.fenty = Button(self, text='Fenty', fg='blue', command = self.compare())
        self.fenty.pack(side='left')
        self.lancome = tk.Button(self, text='Lancome', fg='blue', command = self.compare())
        self.lancome.pack(side='left')
        self.dior = tk.Button(self, text='Dior', fg='blue', command = self.compare())
        self.dior.pack(side='center left')


# In[128]:


if __name__ == '__main__':
    root =Tk()
    root.title("Make-up Matcher")
    root.geometry("500x500")
    app = user_inf(master=root)
    root.mainloop()


# In[ ]:





# In[ ]:




