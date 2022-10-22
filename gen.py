from tkinter import *
import tkinter.font as tkFont
import random

root = Tk()

def GButton_998_command():
    tam = lol.get()
    caracter = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ&*(){}[]/\?!@#$abcdefghijklmnopqrstuvwxyz"
    contra = "".join(random.sample(caracter, tam))
    with open('passwords.txt', 'w') as passwords:
        passwords.write(contra)
    passwords.close()
    GLabel_565=Label(root)
    GLabel_565["bg"] = "#000000"
    ft = tkFont.Font(family='Times',size=10)
    GLabel_565["font"] = ft
    GLabel_565["fg"] = "#00ff00"
    GLabel_565["justify"] = "center"
    GLabel_565["text"] = contra
    GLabel_565.place(x=60,y=210,width=240,height=60)
    

#setting title
root.title("Password Generator")
#setting window size
width=366
height=381
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

GLabel_352=Label()
GLabel_352["bg"] = "#000000"
ft = tkFont.Font(family='Times',size=10)
GLabel_352["font"] = ft
GLabel_352["fg"] = "#e60808"
GLabel_352["justify"] = "center"
GLabel_352["text"] = ""
GLabel_352.place(x=0,y=0,width=366,height=381)

lol = IntVar()
en=Entry(textvariable=lol)
en.place(x=60,y=80,width=230,height=46)
en["fg"] = "#333333"
en["borderwidth"] = "1px"
en["justify"] = "center"
ft = tkFont.Font(family='Times',size=10)
en["font"] = ft

GLabel_612=Label(root)
ft = tkFont.Font(family='Times',size=11)
GLabel_612["font"] = ft
GLabel_612["bg"] = "#000000"
GLabel_612["fg"] = "#ff0000"
GLabel_612["justify"] = "center"
GLabel_612["text"] = "Password lenght (Maximum 77):"
GLabel_612.place(x=80,y=40,width=190,height=30)

GButton_998=Button(root)
GButton_998["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Times',size=12)
GButton_998["font"] = ft
GButton_998["fg"] = "#000000"
GButton_998["justify"] = "center"
GButton_998["text"] = "Generate password"
GButton_998.place(x=110,y=140,width=144,height=37)
GButton_998["command"] = GButton_998_command

root.mainloop()
