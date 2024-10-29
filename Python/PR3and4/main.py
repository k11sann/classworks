import tkinter as tk
from tkinter import PhotoImage
import math
from tkinter import *

root = tk.Tk()

root.title("Практическая №3.4 ИС-22/9-П Субботин Даниэль Александрович")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 900
window_height = 650
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.iconphoto(False, PhotoImage(file="logo.png")) #логотип
root.configure(background = '#765085')
root.grid()

'''--------Functions-------'''

def mult():
    print("meow")
    x1 = float(entryX1.get())
    x2 = float(entryX2.get())
    res = float(x1*x2)
    print(res)
    entryX1.delete(0, END)
    entryX2.delete(0, END)
    entryX1.insert(0,str("%.2f" % round(res, 2)))

def div():
    print("meow")
    x1 = float(entryX1.get())
    x2 = float(entryX2.get())
    res = float(x1/x2)
    print(res)
    entryX1.delete(0, END)
    entryX2.delete(0, END)
    entryX1.insert(0,str("%.2f" % round(res, 2)))

def sum():
    print("meow")
    x1 = float(entryX1.get())
    x2 = float(entryX2.get())
    res = x1+x2
    print(res)
    entryX1.delete(0, END)
    entryX2.delete(0, END)
    entryX1.insert(0,str("%.2f" % round(res, 2)))

def minus():
    print("meow")
    x1 = float(entryX1.get())
    x2 = float(entryX2.get())
    res = x1-x2
    print(res)
    entryX1.delete(0, END)
    entryX2.delete(0, END)
    entryX1.insert(0,str("%.2f" % round(res, 2)))

def calc_pow():
    print("meow")
    x1 = float(entryX1.get())
    x2 = float(entryX2.get())
    res = pow(x1,x2)
    print(res)
    entryX1.delete(0, END)
    entryX2.delete(0, END)
    entryX1.insert(0,str("%.2f" % round(res, 2)))

def calc_sqrt():
    print("meow")
    x1 = float(entryX1.get())
    res = math.sqrt(x1)
    print(res)
    entryX1.delete(0, END)
    entryX2.delete(0, END)
    entryX1.insert(0,str("%.2f" % round(res, 2)))
    
def clear():
    entryX1.delete(0, END)
    entryX2.delete(0, END)
    



'''--------Label-------'''

mainTitleLabel = tk.Label(root, text="Калькулятор", font=("Courier New", 15), background="#a688be", foreground="#53445f") #титул
mainTitleLabel.place(relx=0.5, rely=0.01)
mainTitleLabel.pack(anchor="center",padx=8, pady= 8)



'''--------Buttons-------'''
xWidth = 30 #длина
yHeight = 3 #высота
entryX1 = tk.Entry(root, width=xWidth//2, font=("arial", yHeight*10), fg="white", bg="black")
entryX2 = tk.Entry(root, width=xWidth//2, font=("arial", yHeight*10), fg="white", bg="black")

entryX1.pack(anchor='center')
entryX2.pack(anchor='center')
entryX1.place(x=50, relx=0, y=50)
entryX2.place(x=50, relx=0.5, y=50)

buttonSum = tk.Button(root, text="Плюс +", width=xWidth, height=yHeight, command=sum)
buttonMinus = tk.Button(root, text="Минус -", width=xWidth, height=yHeight, command=minus)
buttonDiv = tk.Button(root, text="Деление /", width=xWidth, height=yHeight, command=div)
buttonMult = tk.Button(root, text="Умножение *", width=xWidth, height=yHeight, command=mult)
buttonClear = tk.Button(root, text="CE", width=xWidth, height=yHeight, command=clear)
buttonPow = tk.Button(root, text="В степень ^n", width=xWidth, height=yHeight, command=calc_pow)
buttonSqrt = tk.Button(root, text="Корень √", width=xWidth, height=yHeight, command=calc_sqrt)

allButtons = [buttonSum, buttonMinus, buttonMult, buttonDiv,buttonPow,buttonSqrt,buttonClear] #массив buttons
allEntry = [entryX1, entryX2] #массив entry
meow = 24 #размер
for i in range(len(allButtons)): # вычисляет длину массива чтобы применялось к объектам
    if i==1:
        n=meow*yHeight
    else:
        n=int(meow*i*yHeight)
    allButtons[i].place(x=50, y=150+n)

root.mainloop()
