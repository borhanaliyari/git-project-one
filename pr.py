from tkinter import *
import random

class Rand(Tk):
    def __init__(self) :
        super().__init__()
        self.title("Random Game for children")
        self.minsize(640,520)
        self.configure(background="gray")
        self.ui()

    def ui(self):
        self.label = Label(text = "Welcome to your Game",font=("Arial",25),background="black",foreground="white")
        self.label.pack()
        but = Button(text = "click",background="red",font=("Arial",12),command=self.button)
        but.pack()
        self.label1 = Label(text = "",background="green",font=("Arial",30))
        self.label1.pack()
        label2 = Label(text = "do you love it",background="red",font=("Arial",50),foreground="yellow")
        label2.pack()


    def button(self):
        self.label1.config(text="salamchalem",padx=25,pady=15)
            
        












play = Rand()
play.mainloop()