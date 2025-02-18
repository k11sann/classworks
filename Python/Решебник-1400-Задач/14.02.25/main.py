# 14/02/25 Субботин 

print("6.23 ----------------")
class lijnik:
    def __init__(self):
        self.day = 1
        self.raston = 10
        self.total_raston = 0

    def run_next_day(self):
        self.raston *= 1.1
        self.day += 1
        self.total_raston += self.raston

    def found_days_to_the_goal(self):
        day_20km = None
        day_total_100km = None

        while True:
            if not day_20km and self.raston > 20:
                day_20km = self.day
            
            if not day_total_100km and self.total_raston > 100:
                day_total_100km = self.day
                
            if day_20km is not None and day_total_100km is not None:
                break

            self.run_next_day()
        
        return day_20km, day_total_100km

лыжник = lijnik()
day_20km, day_total_100km = лыжник.found_days_to_the_goal()

print(f"Лыжник пробежит более 20 км на {day_20km} день.")
print(f"Пробег превысит 100 км на {day_total_100km} день.")

print("6.41 ----------------")
class Number:
    def __init__(self, number):
        self.digits = [int(digit) for digit in str(number)]
        
    def get_max(self):
        return max(self.digits)
    
    def get_min(self):
        return min(self.digits)
    
number = int(input("Введите натуральное число: "))
analyz = Number(number)

print(f"Максимальная цифра: {analyz.get_max()}")
print(f"Минимальная цифра: {analyz.get_min()}")

print("6.48 ----------------")
class Number:
    def __init__(self, number):
        self.number = str(number)

    def get_max_odd_digit(self):
        max_odd = -1
        for char in self.number:
            digit = int(char)
            if digit % 2 == 1 and digit > max_odd:
                max_odd = digit
        return max_odd

    def get_first_min_digit(self):
        min_digit = '9'
        position = 0
        for i, char in enumerate(self.number):
            if char < min_digit:
                min_digit = char
                position = i + 1
        return position

number = 123456789
analyzer = Number(number)
max_odd_digit = analyzer.get_max_odd_digit()
first_min_digit_pos = analyzer.get_first_min_digit()
print(f"Максимальная нечетная цифра: {max_odd_digit}")
print(f"Минимальной цифра: {first_min_digit_pos}")

print("7.23 ----------------")
class Product:
    def __init__(self, *args):
        self.numbers = args

    def product(self):
        product = 1
        for number in self.numbers:
            product *= number
        return product < 10000

a1, a2, a3, a4, a5, a6, a7, a8 = 1, 2, 3, 4, 5, 6, 7, 8
checker = Product(a1, a2, a3, a4, a5, a6, a7, a8)
if checker.product():
    print("Произведение чисел меньше 10 000.")
else:
    print("Произведение чисел не меньше 10 000.")
    
print("7.30 ----------------")

class Item:
    def __init__(self, mass):
        self.mass = mass


class Collection:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_average_mass(self):
        if not self.items:
            return 0
        return sum(item.mass for item in self.items) / len(self.items)

collection = Collection()
collection.add_item(Item(100))
collection.add_item(Item(150))
collection.add_item(Item(200))
average_mass = collection.get_average_mass()
print(f"Средняя масса предметов: {average_mass} g")

print("7.42 ----------------")

class Number:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate(self):
        return sum(num for num in self.numbers if num % 2 == 0)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
calculator = Number(numbers)
result = calculator.calculate()
print(f"Сумма четных чисел: {result}")

print("7.78 ----------------")

class GradeCounter:
    def __init__(self):
        self.grades_count = {
            'fives': 0,
            'fours': 0,
            'threes': 0,
            'twos': 0
        }

    def count_grades(self, grades):
        for grade in grades:
            if grade == 5:
                self.grades_count['fives'] += 1
            elif grade == 4:
                self.grades_count['fours'] += 1
            elif grade == 3:
                self.grades_count['threes'] += 1
            else:
                self.grades_count['twos'] += 1

    def results(self):
        print("Пятерки:", self.grades_count['fives'])
        print("Четверки:", self.grades_count['fours'])
        print("Тройки:", self.grades_count['threes'])
        print("Двойки:", self.grades_count['twos'])

grades = [5, 4, 3, 2, 5, 4, 3, 2, 5]

counter = GradeCounter()
counter.count_grades(grades)
counter.results()
