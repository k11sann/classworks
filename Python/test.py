#С кайфом

a = 1
b = 2
text = None
if (a > 0 and b > 0):
    print("1")
    print("2")
    print("3")
    print(a,b)
else:
    print("Ну бывает")
print("eh")

for i in range(5):
    try:
       text =int(input("Введите текст -> "))
       break
    except ValueError:
        print("Ошибка")
if (text!=None):
    print(text)
else:
    print("Успешно")