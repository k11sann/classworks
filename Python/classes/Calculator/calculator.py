class Calculator:
    def __init__(self):
        self.num1=0
        
    def calc_sum(self, num2):
        self.num1+=num2
        return self.num1
    
    def calc_multiply(self,num2):
        self.num1*=num2
        return self.num1
    
    def calc_subtract(self,num2):
        self.num1-=num2
        return self.num1
    
    def calc_divide(self,num2):
        if num2!=0:
            self.num1/=num2
            return self.num1
        else:
            return "ОШИБКА"
    
calc=Calculator()
