class TriangleChecker:
    def __init__(self, a0, b0, c0):
        self.a=a0
        self.b=b0
        self.c=c0
    
    def is_triangle(self):
        try:                     
            larg = max(self.a, self.b, self.c)
            if self.a<0 or self.b<0 or self.c<0:
                return "С отрицательными числами ничего не выйдет!"
            else:
                if self.a+self.b+self.c-larg>larg:
                    return "Ура, можно построить треугольник!"
                else:
                    return "Жаль, но из этого треугольник не сделать"
        except:
            return "Нужно вводить только числа!"
            
prg=TriangleChecker(30,40,15)
print(prg.is_triangle())
