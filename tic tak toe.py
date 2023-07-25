from tkinter import *
import random
from tkinter import messagebox


word = random.choice(["X","O"])
color = {"O" : "blue","X":"red"}
board = [[],[],[]]


class Game(Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic tak toe")
        self.minsize(445,400)
        self.configure(background="gray")
        self.ui()

    def ui(self):
        self.button1 = Button(self,text = "",bg="light blue",font=("Arial",30),width=6 , height=3,command=lambda:self.click)
        self.button1.grid(row =0 , column=0)
        self.button2 = Button(self,text = "",bg="light blue",font=("Arial",30),width=6 , height=3,command=lambda:self.click)
        self.button2.grid(row =0 , column=1)
        self.button3 = Button(self,text = "",bg="light blue",font=("Arial",30),width=6 , height=3,command=lambda:self.click)
        self.button3.grid(row =0 , column=2)
        self.button4 = Button(self,text = "",bg="light blue",font=("Arial",30),width=6 , height=3,command=lambda:self.click)
        self.button4.grid(row =1 , column=0)
        self.button5 = Button(self,text = "",bg="light blue",font=("Arial",30),width=6 , height=3,command=lambda:self.click)
        self.button5.grid(row =1 , column=1)
        self.button6= Button(self,text = "",bg="light blue",font=("Arial",30),width=6 , height=3,command=lambda:self.click)
        self.button6.grid(row =1, column=2)
        self.button7 = Button(self,text = "",bg="light blue",font=("Arial",30),width=6 , height=3,command=lambda:self.click)
        self.button7.grid(row =2 , column=0)
        self.button8 = Button(self,text = "",bg="light blue",font=("Arial",30),width=6 , height=3,command=lambda:self.click)
        self.button8.grid(row =2 , column=1)
        self.button9 = Button(self,text = "",bg="light blue",font=("Arial",30),width=6 , height=3,command=lambda:self.click)
        self.button9.grid(row =2 , column=2)
        




    

        





















play = Game()
play.mainloop()