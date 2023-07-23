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
        self.label1 = Label(text = "",background="pink",font=("Arial",30))
        self.label1.pack()
        label2 = Label(text = "do you love it",background="red",font=("Arial",50))
        label2.pack()


    def button(self):
        num = "09"
        rand_num = random.randint(0,20)
        for i in num:
            num += str(rand_num)
        self.label1.config(text=num)
            
        












play = Rand()
play.mainloop()