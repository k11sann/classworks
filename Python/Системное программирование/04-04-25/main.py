import math, random

#10.1
#10.3
#10.8
#10.11

class Quest:
    def __init__(self):
        pass

    def genFloat(self, x0, x1, y=1):
        y = int(y)
        numbers = []
        for i in range(y):
            numbers.append(random.uniform(x0,x1))
        return numbers
    
def readList(list):
    num = 1
    for item in list:
        print(f"{num}. {item}")
        num+=1

    
main = Quest()
main_list = []

print("---10.1---")
print("---а---")
main_list = []
main_list=main.genFloat(0, 1, 8)
readList(main_list)
print("---б---")
main_list = []
triger = False
while (triger==False):
    try:
        num = input("Введите кол-во генераций для задания Б : ")
        main_list=main.genFloat(0, 1, int(num))
        triger=True
    except:
        pass
readList(main_list)
print("---в---")
main_list = []
main_list=main.genFloat(25, 26, 15)
readList(main_list)
print("---г---")
main_list = []
main_list=main.genFloat(0, 15, 20)
readList(main_list)
print("---д---")
triger = False
while (triger==False):
    try:
        num1 = input("Введите знач. А для задания д : ")
        num2 = input("Введите знач. Б для задания д : ")
        num3 = random.randint(1, int(num1))
        print(f"Кол-во генераций будет максимум {num1}, а само число ген. {num3}")
        main_list = []
        main_list=main.genFloat(int(num1), int(num2), int(num3))
        triger=True
    except:
        pass
readList(main_list)
print("---е---")
main_list = []
main_list=main.genFloat(-40, 40, 10)
readList(main_list)
print("---ж---")
triger = False
while (triger==False):
    try:
        numM = input("Введите знач. М для задания ж : ")
        numK = random.randint(1, int(numM))
        num1 = input("Введите знач. А для задания ж : ")
        num2 = input("Введите знач. Б для задания ж : ")
        print(f"Значение K : {numK}, сген. от 1 до {int(numM)}")
        main_list = []
        main_list=main.genFloat(int(num1), int(num2), int(numK))
        triger=True
    except:
        pass
readList(main_list)


class Quest:
    def __init__(self):
        pass

    def getCoin(self):
        coin_r = ""
        coin_n = random.randint(0,1)
        if coin_n==1:
            coin_r = "Решка"
        else:
            coin_r = "Орел"
        return coin_r
    
    def funny(self, x0, y0):
        coin_need = x0
        coin_f = y0
        coin_try = 0
        while ()

print("---10.8---")
main = Quest()
main.getCoin()
print(main.getCoin())
