from tkinter import *
import random

class Rand(Tk):
    def __init__(self) :
        super().__init__()
        self.title("Random Game")
        self.minsize(640,520)
        self.configure(background="gray")
        self.ui()

    def ui(self):
        self.label = Label(text = "Welcome to your Game",font=("Arial",25),background="black",foreground="white")
        self.label.pack()
        but = Button(text = "click",background="red",font=("Arial",12),command=self.button)
        but.pack()


    def button(self):
        self.label.config(text="you can play a lot" )
        












play = Rand()
play.mainloop()