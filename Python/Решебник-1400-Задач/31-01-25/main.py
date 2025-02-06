#3.23-3.26
#4.2-4.8

import math

print("----3.23")
class Numb():
    def __init__(self):
        pass

    def reverse(self, num):
        num = str(num)
        a = num[len(num)-1]
        num = num[:-1]
        num = a+num
        return num
    
main=Numb()
print("Число 123")
print(main.reverse(123))

print("----3.24")
class Numb():
    def __init__(self):
        pass

    def reverse(self, num):
        num = str(num)
        a = num[0]
        b = num[1]
        num = num[len(num)-1]
        num = b+a+num
        return num
    
main=Numb()
print("Число 123")
print(main.reverse(123))

print("----3.25")
class Numb(): # 3 24
    def __init__(self):
        pass

    def reverse(self, num):
        num = str(num)
        a = num[1]
        b = num[2]
        num = num[0]
        num = num+b+a
        return num
    
main=Numb()
print("Число 123")
print(main.reverse(123))

print("----3.26")
class Combinator():
    def __init__(self):
        pass

    def combo(self, num):
        if len(str(num))>3:
            print("Введено большое число")
        else:
            num = str(num)
            a = num[0]
            b = num[1]
            c = num[2]
            combo_dict = {
                1:a+b+c,
                2:a+c+b,
                3:b+a+c,
                4:b+c+a,
                5:c+a+b,
                6:c+b+a,
            }
            for i in range(len(combo_dict)):
                i+=1
                print(combo_dict[i])
    
main=Combinator()
print("Число 123")
main.combo(123)

print("----4.2")
class Yravnenie():
    def __init__(self):
        pass

    def exapmple1(self, x): # 4.2
        if x>0:
            y = math.sin(x)
            y = math.pow(y,2)
            return y
        else:
            y = math.pow(x,2)
            y = math.sin(y)
            y = y*2
            y= 1-y
            return y
        
    def exapmple2(self, x): # 4.3
        if x>0:
            y = math.pow(x,2)
            y = math.sin(y)
            return y
        else:
            y = math.sin(x)
            y = math.pow(y,2)
            y = y*2
            y = 1+y
            return y
            
    
main=Yravnenie()
print(main.exapmple1(120))
print("----4.3")
print(main.exapmple2(102))

print("----4.4")
class Tochka():
    def __init__(self, x0, y0):
        if y0 == None:
            y0
        self.x=x0
        self.y=y0

    def sideX(self, x):
        if x<self.x:
            return f"Число: {x}, сектор I"
        elif x>self.x:
            return f"Число: {x}, сектор II"
        else:
            return f"Число: {x}, Между I и II"
        
    def sideY(self, y):
        if y<self.y:
            return f"Число: {y}, сектор II"
        elif y>self.y:
            return f"Число: {y}, сектор I"
        else:
            return f"Число: {y}, Между I и II"

    
main=Tochka(4,3)
print("Точка 4 по X")
print(main.sideX(3))
print(main.sideX(4))
print(main.sideX(5))
print("----4.5")
print("Точка 3 по Y")
print(main.sideY(2))
print(main.sideY(3))
print(main.sideY(4))

print("----4.6")
class Coord():
    def __init__(self):
        pass

    def checkFunc(self, num):
        if num % 2 == 1 :
            return num * -1
        else:
            return num
    
main=Coord()
print("А")
print("X = 2; Y = "+str(main.checkFunc(2)))
print("Б")
print("X = 3; Y = "+str(main.checkFunc(3)))

print("----4.7")
class ZnachFunc():
    def __init__(self):
        pass
    
    def findFunc(self, x):
        return self.findF(self.findK(x), x)

    def findK(self, x):
        if math.sin(x)<0:
            return math.pow(x,2)
        else:
            return abs(x)

    def findF(self, k, x):
        if k<x:
            return k*x
        else:
            return k+x

    
main=ZnachFunc()
num = 6
print("x = "+str(num))
print("k = "+str(main.findK(num)))
print("f = "+str(main.findFunc(num)))

print("----4.8")
class ZnachFunc():
    def __init__(self):
        pass
    
    def findFunc(self, x):
        return self.findF(self.findK(x), x)

    def findK(self, x):
        if math.sin(x)>=0:
            return math.pow(x,2)
        else:
            return abs(x)

    def findF(self, k, x):
        if x<k:
            return abs(x)
        else:
            return k*x

    
main=ZnachFunc()
num = 12
print("x = "+str(num))
print("k = "+str(main.findK(num)))
print("f = "+str(main.findFunc(num)))