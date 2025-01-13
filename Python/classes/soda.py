class Soda:
    def __init__(self):
        self.type = 0
        
    def addType(self, number):
        self.type=number
          
    def show_my_drink(self):
        match self.type:
            case 1:
                return "Газировка ВИШНЁВАЯ"
            case 2:
                return "Газировка ЛИМОННАЯ"
            case 3:
                return "Газировка КОКИ-КОЛА"
            case _:
                return "ОБЫЧНАЯ ГАЗИРОВКА"
        
            
soda=Soda()
soda.addType(2)
print(soda.show_my_drink())
        
