# 2.13-2.18
# 3.29-3.31
#  4.11-4.14

print("/=/=/=/=/=/=/=/=/=/=/=/= 2.13")
class Quest:
    def __init__(self,a0,b0):
        self.a = a0
        self.b = b0

    def yravn(self):
        if self.a!=0:
            x=-self.b
            x=x/self.a
            return x
        else:
            return "Нельзя решить уравнение"

main=Quest(6,8)
print(main.yravn())


