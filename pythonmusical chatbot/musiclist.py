from tkinter import *
from simplechatbot import *
from magic import *
from shuffling import *
from guitar import *


def start(root):
    root.title("screen1")
    beatboxing = Button(root, text="beatboxing ", width=20, command=lambda: change(root)).grid(row=1, column=1)
    magic = Button(root, text="magic", width=20, command=lambda: change1(root)).grid(row=1, column=3)
    drum = Button(root, text="drummer", width=20, command=lambda: change2(root)).grid(row=2, column=1)
    shufflingdance = Button(root, text="dance", width=20, command=lambda: change3(root)).grid(row=2, column=3)


def change(root):
    root.destroy()
    fun()


def change1(root):
    root.destroy()
    mag()


def change2(root):
    root.destroy()
    dr()


def change3(root):
    root.destroy()
    shuff()


def call():
    root = Tk()
    start(root)
    root.mainloop()


call()
