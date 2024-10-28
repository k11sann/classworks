import tkinter as tk
from tkinter import PhotoImage, Canvas

root = tk.Tk()

root.title("Практическая №3 ИС-22/9-П Субботин Даниэль Александрович")

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

def sum():
    print("meow")
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    res = 0
    allXs= [x1,x2,x3,x4]
    allEntry = [entrySum, entryMult, entryMax, entryMin] #массив entry
    for i in range(len(allEntry)):
        try:
            allXs[i] = int(allEntry[i].get())
            print(allXs[i])
            res = res+allXs[i]
        except ValueError:
            allXs[i] = 0
            res = res+allXs[i]
    print(res)
    mainTitleLabel["text"]="Результат суммы : "+str(res)

def mult():
    print("meow")
    x1 = 1
    x2 = 1
    x3 = 1
    x4 = 1
    res = 1
    allXs= [x1,x2,x3,x4]
    allEntry = [entrySum, entryMult, entryMax, entryMin] #массив entry
    for i in range(len(allEntry)):
        try:
            allXs[i] = int(allEntry[i].get())
            print(allXs[i])
            res = res*allXs[i]
        except ValueError:
            print("Отсутствует число")
    print(res)
    mainTitleLabel["text"]="Результат умножения : "+str(res)

def max():
    print("meow")
    x1 = "none"
    x2 = "none"
    x3 = "none"
    x4 = "none"
    res = 0
    allXs= [x1,x2,x3,x4]
    allEntry = [entrySum, entryMult, entryMax, entryMin] #массив entry
    for i in range(len(allEntry)):
        try:
            allXs[i] = int(allEntry[i].get())
            print(allXs[i])
        except ValueError:
            allXs[i] = 0
            print("Отсутствует число")
    res=allXs[0]
    for val in allXs:
        if val!="none":
            if val>res:
                res=val
    print(res)
    mainTitleLabel["text"]="Максимальное : "+str(res)

def min():
    print("meow")
    x1 = "none"
    x2 = "none"
    x3 = "none"
    x4 = "none"
    res = 0
    allXs= [x1,x2,x3,x4]
    allEntry = [entrySum, entryMult, entryMax, entryMin] #массив entry
    for i in range(len(allEntry)):
        try:
            allXs[i] = int(allEntry[i].get())
            print(allXs[i])
        except ValueError:
            allXs[i] = "none"
            print("Отсутствует число")
    res=allXs[0]
    for val in allXs:
        if val!="none":
            if val<res:
                res=val
    print(res)
    mainTitleLabel["text"]="Минимальное : "+str(res)
    



'''--------Label-------'''

canvas = Canvas(root, width=160, height=160, background='#765085')
image_Label = PhotoImage(file="logoTitle.png").subsample(2,2)
canvas.create_image(0,0,anchor='nw', image=image_Label)
canvas.pack()
canvas.place(x=40,y=60)

mainTitleLabel = tk.Label(root, text="Ожидается результат!", font=("Courier New", 15), background="#a688be", foreground="#53445f") #титул
mainTitleLabel.place(relx=0.5, rely=0.01)
mainTitleLabel.pack(anchor="center",padx=8, pady= 8)



'''--------Buttons-------'''
xWidth = 30 #длина
yHeight = 3 #высота
entrySum = tk.Entry(root, width=xWidth//2, font=("arial", yHeight*10), fg="white", bg="black") # первый участник
entryMult = tk.Entry(root, width=xWidth//2, font=("arial", yHeight*10), fg="white", bg="black") # второй участник
entryMax = tk.Entry(root, width=xWidth//2, font=("arial", yHeight*10), fg="white", bg="black") # третий участник
entryMin = tk.Entry(root, width=xWidth//2, font=("arial", yHeight*10), fg="white", bg="black") # третий участник

buttonSum = tk.Button(root, text="Сумма", width=xWidth, height=yHeight, command=sum)
buttonMult = tk.Button(root, text="Произведение", width=xWidth, height=yHeight, command=mult)
buttonMax = tk.Button(root, text="Максимум", width=xWidth, height=yHeight, command=max)
buttonMin = tk.Button(root, text="Минимум", width=xWidth, height=yHeight, command=min)

allButtons = [buttonSum, buttonMult, buttonMax, buttonMin] #массив buttons
allEntry = [entrySum, entryMult, entryMax, entryMin] #массив entry
meow = 24 #размер
for i in range(len(allButtons)): # вычисляет длину массива чтобы применялось к объектам
    if i==1:
        n=meow*yHeight
    else:
        n=int(meow*i*yHeight)
    allButtons[i].place(x=280, y=40+n)

for i in range(len(allEntry)): # вычисляет длину массива чтобы применялось к объектам
    if i==1:
        n=meow*yHeight
    else:
        n=int(meow*i*yHeight)
    allEntry[i].place(x=560, y=40+n)

root.mainloop()