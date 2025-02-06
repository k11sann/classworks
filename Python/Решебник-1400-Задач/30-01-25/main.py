print("---- 3.1")
class Perevod: # 3.1 3.2
    def __init__(self):
        pass

    def metr(self, num):
        return num/100
        

main=Perevod()
print(str(main.metr(300))+" метров")
print("---- 3.2")
print(str(main.metr(500))+" центнеров")

print("---- 3.3")
class TimeDay:
    def __init__(self, days):
        self.days = days

    def weeks(self):
        return self.days//7
    
main=TimeDay(234)
print(str(main.weeks())+" недель")

print("---- 3.4")
class School:
    def __init__(self):
        self.students = 0
        self.apples = 0
        self.applesTo = 0
        self.bak = 0

    def getApples(self, student, apples):
        self.students = student
        self.apples = apples
        if (self.students>self.apples):
            self.applesTo = self.students - self.apples
            self.bak = self.apples - self.applesTo
        else:
            self.applesTo = self.apples//self.students
            self.bak = abs(self.applesTo*self.students - self.apples)
    
    def result(self):
        print(str(self.students)+" Учеников\n"+str(self.apples)+" Яблок")
        print(str(self.applesTo)+" Яблока каждому ученику\n"+str(self.bak)+" Остаток в корзине")
    
main=School()
main.getApples(14,14)
main.result()

print("---- 3.5")
class Treygol:
    def __init__(self,x0,y0):
        self.x = x0
        self.y = y0
        self.s = 0

    def getSquares(self, need):
        res = min(self.x,self.y)
        self.s = res//need
        return self.s

    
    def result(self):
        print("Стороны "+str(self.x)+"x"+str(self.y))
        print(str(self.s)+" получится квадратов")
    
main=Treygol(543,130)
main.getSquares(130)
main.result()

print("---- 3.6")
class Train:
    def __init__(self,x0,y0):
        self.kype = x0
        self.mest = y0
        self.s = 0

    def getNumber(self, mesto):
        self.s = (mesto+self.mest-1)//self.mest

    
    def result(self):
        print("№ купе : "+str(self.s))
    
main=Train(9,4)
main.getNumber(5)
main.result()

print("---- 3.12")
class Flat:
    def __init__(self,x0,y0):
        self.floors = x0
        self.flats = y0
        self.s = 0

    def getNumber(self, flat):
        self.s = (flat+self.flats-1)//self.flats

    
    def result(self):
        print("№ этажа : "+str(self.s))
    
main=Flat(5,4)
main.getNumber(5)
main.result()

print("---- 3.14")
class Flat2:
    def __init__(self,x0,y0,z0):
        self.floors = x0
        self.flats = y0
        self.bad = z0
        self.s = 0

    def getFloor(self, num):
        if num<self.floors*self.flats:
            return (num+self.floors-1)//self.floors
        else:
            return "Слишком большое число"

    def getBad(self, num):
        if num<self.flats*self.floors*self.bad:
            return (num+self.flats-1)//self.flats//self.bad
        else:
            return "Слишком большое число"
    
main=Flat2(9,6, 4)
print(str(main.flats*main.floors)+" все квартиры в 1 подъезде")
print(str(main.getFloor(5))+" этаж")
print(str(main.getBad(56))+" подъезд")

print("---- 3.19")
class Program1:
    def __init__(self):
        pass

    def res(self, num):
        num = str(num)
        s=""
        for i in range(len(num)):
            if i>len(num)-2:
                s = s+num[i]
            else:
                s = s+num[i]+", "
        return s
    
main=Program1()
print(main.res(123))

print("---- 3.27")
class Program2:
    def __init__(self):
        pass

    def res(self, num):
        num = str(num)
        s=0
        for i in range(len(num)):
            s = s+int(num[i])
        return s
    
main=Program2()
print(main.res(input()))