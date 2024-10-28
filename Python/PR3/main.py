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
root.grid()

'''--------Functions-------'''

def result():
    print("meow")
    try: # проверка получения значений
        x1 = int(JumpButton1.get())
        x2 = int(EatButton1.get())
        x3 = int(BeatyButton1.get())
        LabelBall1["text"] = x1+x2+x3
    except ValueError: # иначе будет Н/Б = Нет Баллов
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

    current = 0 # текущие баллы у участника по циклу
    prev = 0 #баллы прошлого участника
    champ = 0 # баллы чемпиона
    champName = "Чемпион не определён" # имя чемпиона
    for i in range(len(Balls)): # цикл по количеству длины массива Bals
        if Balls[i]["text"]!="Н/Б": # если текст баллов не равен НБ, то будет выполняться условие
            current=int(Balls[i]["text"])
            if current > champ: # если текущее значение больше чем чемпиона, то текущее становится чемпионом
                champ = current
                champName = "Победитель : "+str(allNamesX[i+1]["text"])+"; с таким количеством очков : "+str(Balls[i]["text"])
                print(str(allNamesX[i+1]))
                prev = current
            elif current == prev: # если имеют одинаковое количество баллов
                current = 0
                prev = 0
                champ = 0
                champName = "Участники имеют одинаковое количество баллов, нет победителя"
    print(str(current)+": cureent")
    print(str(prev)+": prev")
    print(str(champ)+": champ balls")

    LabelChampion["text"] = champName # установка имени после цикла
            
        

    



'''--------Label-------'''
canvas = Canvas(root, width=256, height=256)
image_Label = PhotoImage(file="logoTitle.png").subsample(2,2)
canvas.create_image(0,0,anchor='nw', image=image_Label)
canvas.pack()
canvas.place(x=40,y=100)

mainTitleLabel = tk.Label(root, text="Соревнование по квадробингу", font=("Courier New", 15), background="#a688be", foreground="#53445f") #титул
mainTitleLabel.place(relx=0.5, rely=0.01)
mainTitleLabel.pack(anchor="center",padx=8, pady= 8)

LabelName1 = tk.Label(root, text="Марат", font=("Courier New", 9)) #имена
LabelName2 = tk.Label(root, text="Лейсан", font=("Courier New", 9))
LabelName3 = tk.Label(root, text="Алексей", font=("Courier New", 9))

LabelAmounts = tk.Label(root, text="Кол-во", font=("Courier New", 9)) #критерии
LabelJump = tk.Label(root, text="Прыжки в минуту", font=("Courier New", 9))
LabelEat = tk.Label(root, text="Корм за минуту", font=("Courier New", 9))
LabelBeaty = tk.Label(root, text="Изящность", font=("Courier New", 9))
LabelBalls = tk.Label(root, text="Баллы", font=("Courier New", 9))

LabelBall1 = tk.Label(root, text="", font=("Courier New", 9)) #баллы
LabelBall2 = tk.Label(root, text="", font=("Courier New", 9))
LabelBall3 = tk.Label(root, text="", font=("Courier New", 9))

LabelChampion = tk.Label(root, text="Чемпион не определён", font=("Courier New", 12))

allNamesX = [LabelAmounts, LabelName1, LabelName2, LabelName3] #массив участников
allNamesY = [LabelAmounts, LabelJump, LabelEat, LabelBeaty,LabelBalls] #массив критерий
Balls = [LabelBall1, LabelBall2, LabelBall3] # массив лейблов с баллами



'''--------Buttons-------'''

EatButton1 = tk.Entry(root) # первый участник
EatButton2 = tk.Entry(root) # второй участник
EatButton3 = tk.Entry(root) # третий участник

JumpButton1 = tk.Entry(root)
JumpButton2 = tk.Entry(root)
JumpButton3 = tk.Entry(root)

BeatyButton1 = tk.Entry(root)
BeatyButton2 = tk.Entry(root)
BeatyButton3 = tk.Entry(root)

JumpButtons = [JumpButton1, JumpButton2, JumpButton3]
for i in range(len(allNamesX)): # вычисляет длину массива чтобы применялось к объектам
    if i==0:
        n=0
    else:
        n=190*i
    allNamesX[i].place(x=140+n, y=40)

for i in range(len(allNamesY)): # вычисляет длину массива чтобы применялось к объектам
    if i==1:
        n=50
    else:
        n=50*i
    allNamesY[i].place(x=190, y=40+n)

LabelBall1.place(x=LabelName1.place_info().get("x"), y=LabelBalls.place_info().get("y")) # размещает баллы по участникам
LabelBall2.place(x=LabelName2.place_info().get("x"), y=LabelBalls.place_info().get("y"))
LabelBall3.place(x=LabelName3.place_info().get("x"), y=LabelBalls.place_info().get("y"))
LabelChampion.place(x=int(LabelName2.place_info().get("x"))-200, y=int(LabelBalls.place_info().get("y"))+40) # размещение чемпиона

JumpButton1.place(x=LabelName1.place_info().get("x"), y=LabelJump.place_info().get("y")) #энтри первого участника
JumpButton2.place(x=LabelName2.place_info().get("x"), y=LabelJump.place_info().get("y")) #энтри второго участника
JumpButton3.place(x=LabelName3.place_info().get("x"), y=LabelJump.place_info().get("y")) #энтри третьего участника

EatButton1.place(x=LabelName1.place_info().get("x"), y=LabelEat.place_info().get("y"))
EatButton2.place(x=LabelName2.place_info().get("x"), y=LabelEat.place_info().get("y"))
EatButton3.place(x=LabelName3.place_info().get("x"), y=LabelEat.place_info().get("y"))

BeatyButton1.place(x=LabelName1.place_info().get("x"), y=LabelBeaty.place_info().get("y"))
BeatyButton2.place(x=LabelName2.place_info().get("x"), y=LabelBeaty.place_info().get("y"))
BeatyButton3.place(x=LabelName3.place_info().get("x"), y=LabelBeaty.place_info().get("y"))


resButton = tk.Button(text="Расчитать баллы", command=result) #кнопка результата
resButton.place(x=LabelBalls.place_info().get("x"), y=LabelChampion.place_info().get("y"))

root.mainloop()
