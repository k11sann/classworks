#Субботин ИС-22-9-П 11.09.2024
a = 0
b = 0
while True:
    try:
        print("-----------------------------")
        a = int(input("Введите A значение : "))
        b = int(input("Введите B значение : "))
        break
    except ValueError:
        print("-----------------------------")
        print("Укажите числовое значение!")
while (a!=b):
    if (a>b):
        a=a-b
    else:
        b=b-a
print("-----------------------------")
print("Конечное значение A : ", a)
print("Конечное значение B : ", b)
file = open("res.txt", "w")
file.write("Значение А = " + str(a) + '\n'"Значение B = " + str(b))
file.close()
