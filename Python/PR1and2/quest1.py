import tkinter as tk
from tkinter import ttk
import re
import math

root = tk.Tk()

root.title("Практическая №3 ИС-22/9-П Субботин Даниэль Александрович")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 900
window_height = 650
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

'''functions'''
def is_valid(newval):
    return re.match("^\d{0,4}$", newval) is not None

def result():
    a=int(aButton.get())
    b=int(bButton.get())
    c=int(cButton.get())
    triangleType = "none"
    if a==b and b==c: # Равносторонний треуг
        triangleType = "Равносторонний"
        S=pow(a,2)*math.sqrt(3/4)
        LabelResult["text"] = "Тип треугольника : "+triangleType+", Площадь : "+str(S)
    elif (a==b and b!=c) or (a!=b and b==c): #равнобедренный треуг
        triangleType = "Равнобедренный"
        S=(b*math.sqrt(4*pow(a,2)-pow(c,2)))/4
        LabelResult["text"] = "Тип треугольника : "+triangleType+", Площадь : "+str(S)
    else: #разносторонний
        triangleType = "Разносторонний"
        p=float((a+b+c)/2)
        print(p)
        try:
            S=math.sqrt(p*(p-a)*(p-b)*(p-c))
            LabelResult["text"] = "Тип треугольника : "+triangleType+", Площадь : "+str(S)
        except ValueError:
            LabelResult["text"] = "Тип треугольника : "+triangleType+", Невозможно вычислить площадь"
    print(S)

'''Label'''

LabelA = tk.Label(root, text="A", font=("Courier New", 9))
LabelB = tk.Label(root, text="B", font=("Courier New", 9))
LabelC = tk.Label(root, text="C", font=("Courier New", 9))
LabelA.pack(anchor="center", padx=6, pady=6)
LabelB.pack(anchor="center", padx=6, pady=6)
LabelC.pack(anchor="center", padx=6, pady=6)

LabelResult = tk.Label(root, text="Нажмите на кнопку для результата", font=("Courier New", 9))
LabelResult.place(x=200, y=92)

Labels = [LabelA, LabelB, LabelC]

for i in range(len(Labels)): # вычисляет длину массива чтобы применялось к объектам
    Labels[i].place(x=20+(125*i), y=20)


'''Buttons'''
check = (root.register(is_valid), "%P")

aButton = tk.Entry(validate="key", validatecommand=check)
bButton = tk.Entry(validate="key", validatecommand=check)
cButton = tk.Entry(validate="key", validatecommand=check)

aButton.place(x=LabelA.place_info().get("x"), y=52)
bButton.place(x=LabelB.place_info().get("x"), y=52)
cButton.place(x=LabelC.place_info().get("x"), y=52)

resButton = tk.Button(text="Расчитать какой треугольник", command=result)
resButton.place(x=20, y=92)

root.mainloop()
