#4.10-4.14
#7.1-7.5

import math

print("\n/-/-/-/-/ 4.10")
class Quest():
    def __init__(self):
        pass

    def inKm(self, x):
        return x*0.000305


main=Quest()
print("x = 300 км")
print("y = 300 футов, "+str(main.inKm(300))+" км")
print("Большее : "+str(max(300, main.inKm(300)))+" км")

print("\n/-/-/-/-/ 4.11")
class Quest():
    def __init__(self):
        pass

    def inKmPerHour(self, x):
        return x*3.6


main=Quest()
print("x = 15 км/час")
print("y = 18 м/с, "+str(main.inKmPerHour(18))+" км/ч")
print("Большее : "+str(max(15, main.inKmPerHour(18)))+" км/ч")

print("\n/-/-/-/-/ 4.12")
class Quest():
    def __init__(self):
        pass
    
    def sCircle(self,x):
        return math.pow(x,2)*3.14
    
    def sSquare(self,x):
        return math.pow(x,2)


main=Quest()
print("Радиус = 140, Площадь = "+str(main.sCircle(140)))
print("Сторона = 160, Площадь = "+str(main.sSquare(160)))
print("Большее : "+str(max(main.sCircle(140), main.sSquare(160))))

print("\n/-/-/-/-/ 4.13")
class Quest():
    def __init__(self):
        pass
    
    def pLot(self,m,v):
        return m/v


main=Quest()
print("Масса = 14 кг, Объём  = 256, Плотность = "+str(main.pLot(14,256)))
print("Масса = 27 кг, Объём  = 512, Плотность = "+str(main.pLot(27,512)))
print("Большее : "+str(max(main.pLot(14,256), main.pLot(27,512))))

print("\n/-/-/-/-/ 4.14")
class Quest():
    def __init__(self):
        pass
    
    def omI(self,v,r):
        return v/r


main=Quest()
print("Напряжение = 15, Сопротивление  = 8, Сила тока = "+str(main.omI(15,8)))
print("Напряжение = 9, Сопротивление  = 17, Сила тока = "+str(main.omI(9,17)))
print("Меньший ток : "+str(max(main.omI(15,8), main.omI(8,17))))

print("\n/-/-/-/-/ 7.1")
class Quest():
    def __init__(self):
        pass
    
    def adding(self,a,value):
        adder = a
        for i in range(value):
            a+=adder
        return a


main=Quest()
print("A = 2, Циклов  = 10, Результат = "+str(main.adding(2,10)))

print("\n/-/-/-/-/ 7.2")
class Quest():
    def __init__(self):
        pass
    
    def adding(self,a,value):
        adder = a
        for i in range(value):
            a+=adder
        return a


main=Quest()
print("A = 0.32, Циклов  = 10, Результат = "+str(main.adding(0.32,10)))

print("\n/-/-/-/-/ 7.3")
class Quest():
    def __init__(self):
        pass
    
    def per(self,a,b,c):
        return a+b+c


main=Quest()
print("A = 5, B = 12, C = 18, Результат = "+str(main.per(5,12,18)))

print("\n/-/-/-/-/ 7.4")
class Quest():
    def __init__(self):
        pass
    
    def massList(self,list):
        res = 0
        for i in range(len(list)):
            res+=list[i]
        return res


main=Quest()
print("1пр = 5кг, \n2пр = 14кг, \n3пр = 18кг, \n4пр = 25кг, \nРезультат = "+str(main.massList([5,14,18,25])))

print("\n/-/-/-/-/ 7.5")
class Quest():
    def __init__(self, zp0):
        self.zp = zp0
        self.allZp = 0
    
    def resultAllZp(self,valueWorkers):
        res = 0
        for i in range(valueWorkers):
            res+=self.zp
        self.allZp = res


main=Quest(18900)
main.resultAllZp(32)
print("Зарплата : 18900\nКол-во сотрудников : 32\nРезультат = "+str(main.allZp))

print("\n/-/-/-/-/ 7.10")
class Quest():
    def __init__(self):
        self.sport1 = []
        self.sport2 = []
    
    def setSport1(self, values):
        self.sport1 = values

    def setSport2(self, values):
        self.sport2 = values

    def resultSports(self):
        res_sport1 = 0
        res_sport2 = 0
        for i in range(1,len(self.sport1)):
            res_sport1+=self.sport1[i]

        for i in range(1,len(self.sport2)):
            res_sport2+=self.sport2[i]

        if res_sport1!=res_sport2:
            names_dict = {res_sport1:self.sport1[0], res_sport2:self.sport2[0]}
            print("Первый спортсмен : "+str(res_sport1))
            print("Второй спортсмен : "+str(res_sport2))
            res = max(res_sport1,res_sport2)
            return f"Победитель : {names_dict[res]}, Кол-во баллов : {res}" # я случайно забыл задание и думал нужно было определить победителя....
        else:
            return "Одинаковые баллы"


main=Quest()
main.setSport1(["Первый спортсмен",2,3,5,1,2])
main.setSport2(["Второй спортсмен",5,4,3,2,1])
print(main.resultSports())
