#8.1.
#8.7
#8.11
#8.18.
#9.2
#9.5.
import math

print("/// 8.1 ///")
class Quest():
    def __init__(self, form0):
        self.form = form0
        self.nums = []
        num = 0
        while(num<self.form):
            num+=1
            self.nums.append(num*num)
        print(self.nums)

    def check_n(self, n0):
        num = 0
        print_string = ''
        while(num<len(self.nums) and self.nums[num]<n0):
            if num>0:
                print_string+=f","
            print_string+=f" {self.nums[num]}"
            num+=1
        print(f"Все числа меньшие n({n0}) : {print_string}")

main=Quest(6)
main.check_n(17)

print("/// 8.7 не сделал///")


print("/// 8.11 ///")
class Quest():
    def __init__(self, form0):
        self.form = form0

    def check_max(self, n0):
        print(f"Большие числа n ({n0})")
        num = 1
        for i in range(len(self.form)):
            if self.form[i]>n0:
                print(f"{num} : {self.form[i]} > n ({n0})")
                num+=1

    def check_index(self, i0):
        try:
            print(f"Показать элемент с индексом {i0}")
            print(self.form[i0])
        except IndexError:
            pass

main=Quest([1, 1+1/2, 1+1/2+1/3])
main.check_max(1)
main.check_index(0)

print("/// 8.18 не сделал///")


print("/// 9.2 ///")
class Quest():
    def __init__(self):
        pass

    def table_math(self):
        for i in range(1,10):
            for j in range(1,10):
                print(f"{i} + {j} = {i+j}")

main=Quest()
main.table_math()

print("/// 9.5 ///")
class Quest():
    def __init__(self, workers0, mounth0):
        self.workers = workers0
        self.mounth = mounth0
        self.money_list = []

    def set_money(self):
        for i in range(self.workers):
            money_input=[]
            for j in range(self.mounth):
                m_input=input(f"Введите зарплату работнику №{i+1} за {j+1} месяц: ")
                money_input.append(m_input)
            self.money_list.append([i, money_input])
        
    def print_table(self):
        all_print='Работники    |    Месяц   '
        for i in range(len(self.money_list)):
            all_print+="\n"
            all_print+=str(self.money_list[i][0]+1)+"         |         "
            for j in range(self.mounth):
                all_print+=str(self.money_list[i][1][j])+"  |   "
        print(all_print)

        moneys=0 # общее денег
        for i in range(len(self.money_list)):
            for j in range(self.mounth):
                moneys+=int(self.money_list[i][1][j])
        all_print=f"Общее всем работникам : {moneys}"
        print(all_print)
        moneys=0
        all_print='Работники    |    Зарплата (за квартал)   '
        for i in range(len(self.money_list)):
            all_print+="\n"
            all_print+=str(self.money_list[i][0]+1)+"         |         "
            for j in range(self.mounth):
                moneys+=int(self.money_list[i][1][j])
            all_print+=str(moneys)+"  |   "
        print(all_print)

main=Quest(12, 3)
main.set_money()
main.print_table()


