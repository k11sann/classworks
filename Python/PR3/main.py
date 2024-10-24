import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("Практическая №3 ИС-22/9-П Субботин Даниэль Александрович")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 900
window_height = 650
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.grid()

'''--------Functions-------'''

def result():
    print("meow")
    try:
        x1 = int(JumpButton1.get())
        x2 = int(EatButton1.get())
        x3 = int(BeatyButton1.get())
        LabelBall1["text"] = x1+x2+x3
    except ValueError:
        LabelBall1["text"] = "Н/Б"

    try:
        x1 = int(JumpButton2.get())
        x2 = int(EatButton2.get())
        x3 = int(BeatyButton2.get())
        LabelBall2["text"] = x1+x2+x3
    except ValueError:
        LabelBall2["text"] = "Н/Б"

    try:
        x1 = int(JumpButton3.get())
        x2 = int(EatButton3.get())
        x3 = int(BeatyButton3.get())
        LabelBall3["text"] = x1+x2+x3
    except ValueError:
        LabelBall3["text"] = "Н/Б"

    



'''--------Label-------'''
mainTitleLabel = tk.Label(root, text="Соревнование по квадробингу", font=("Courier New", 15), background="#a688be", foreground="#53445f")
mainTitleLabel.place(x=window_width//4, rely=0.01)
mainTitleLabel.pack(anchor="center",padx=8, pady= 8)

LabelName1 = tk.Label(root, text="Марат", font=("Courier New", 9))
LabelName2 = tk.Label(root, text="Лейсан", font=("Courier New", 9))
LabelName3 = tk.Label(root, text="Алексей", font=("Courier New", 9))
LabelName1.place(x=50, y=40)
LabelName2.place(x=50, y=40)
LabelName3.place(x=50, y=40)

LabelAmounts = tk.Label(root, text="Кол-во", font=("Courier New", 9))
LabelAmounts.place(x=50, y=40)
LabelJump = tk.Label(root, text="Прыжки в минуту", font=("Courier New", 9))
LabelJump.place(x=50, y=40)
LabelEat = tk.Label(root, text="Корм за минуту", font=("Courier New", 9))
LabelEat.place(x=50, y=40)
LabelBeaty = tk.Label(root, text="Изящность", font=("Courier New", 9))
LabelBeaty.place(x=50, y=40)
LabelBalls = tk.Label(root, text="Баллы", font=("Courier New", 9))
LabelBalls.place(x=50, y=40)

LabelBall1 = tk.Label(root, text="", font=("Courier New", 9))
LabelBall2 = tk.Label(root, text="", font=("Courier New", 9))
LabelBall3 = tk.Label(root, text="", font=("Courier New", 9))






'''--------Buttons-------'''

EatButton1 = tk.Entry(root)
EatButton2 = tk.Entry(root)
EatButton3 = tk.Entry(root)

JumpButton1 = tk.Entry(root)
JumpButton2 = tk.Entry(root)
JumpButton3 = tk.Entry(root)

BeatyButton1 = tk.Entry(root)
BeatyButton2 = tk.Entry(root)
BeatyButton3 = tk.Entry(root)



allNamesX = [LabelAmounts, LabelName1, LabelName2, LabelName3]
allNamesY = [LabelAmounts, LabelJump, LabelEat, LabelBeaty,LabelBalls]

JumpButtons = [JumpButton1, JumpButton2, JumpButton3]
for i in range(len(allNamesX)): # вычисляет длину массива чтобы применялось к объектам
    if i==0:
        n=0
    else:
        n=190*i
    allNamesX[i].place(x=20+n, y=40)

for i in range(len(allNamesY)): # вычисляет длину массива чтобы применялось к объектам
    if i==1:
        n=50
    else:
        n=50*i
    allNamesY[i].place(x=20, y=40+n)

LabelBall1.place(x=LabelName1.place_info().get("x"), y=LabelBalls.place_info().get("y")) # размещает баллы по участникам
LabelBall2.place(x=LabelName2.place_info().get("x"), y=LabelBalls.place_info().get("y"))
LabelBall3.place(x=LabelName3.place_info().get("x"), y=LabelBalls.place_info().get("y"))

JumpButton1.place(x=LabelName1.place_info().get("x"), y=LabelJump.place_info().get("y"))
JumpButton2.place(x=LabelName2.place_info().get("x"), y=LabelJump.place_info().get("y"))
JumpButton3.place(x=LabelName3.place_info().get("x"), y=LabelJump.place_info().get("y"))

EatButton1.place(x=LabelName1.place_info().get("x"), y=LabelEat.place_info().get("y"))
EatButton2.place(x=LabelName2.place_info().get("x"), y=LabelEat.place_info().get("y"))
EatButton3.place(x=LabelName3.place_info().get("x"), y=LabelEat.place_info().get("y"))

BeatyButton1.place(x=LabelName1.place_info().get("x"), y=LabelBeaty.place_info().get("y"))
BeatyButton2.place(x=LabelName2.place_info().get("x"), y=LabelBeaty.place_info().get("y"))
BeatyButton3.place(x=LabelName3.place_info().get("x"), y=LabelBeaty.place_info().get("y"))


resButton = tk.Button(text="Расчитать баллы", command=result)
resButton.place(x=20, y=280)

root.mainloop()
