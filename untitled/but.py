

from tkinter import *
import a

class but:



    def __init__(self, x,c,n):
        self.x=x
        self.MyButton = Button(c, text=n)
        self.MyButton['background']="#FFFFFF"
        self.MyButton['foreground']="red"
        self.MyButton['command']=self.MyButton_Click
        self.MyButton.pack({"side":"top", "padx": 10, "pady": 20})



    def MyButton_Click(self):

        print(a.Application.fun(self,self.x))
