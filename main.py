from tkinter import *
import os
a = 64
b = 255
c = 208
def change():
    global a
    global b
    global c
    root.configure(background='#%02x%02x%02x' % (a, b, c))
    if b>0 :
        b= b-1
    else :
        b = 255
    root.after(100,change)

root = Tk()
root.geometry('500x700')

change()
root.mainloop() 
