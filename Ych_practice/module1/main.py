from module_import import Export

import keyboard, time

class User():
    def __init__(self):
        self.role = ""
        self.FIO = ""
        self.login = ""
        self.password = ""

    def get_name(self, num=0):
        fio = self.FIO.split(' ')
        if num>=len(fio):
            return fio[0]
        
        return fio[num]

    def check(self):
        conn = Export.get_base()
        cur = conn.cursor()
        login = f"SELECT login, password, fio, role FROM users WHERE login = '{self.login}' AND password = '{self.password}'"
        cur.execute(login)
        result = cur.fetchone()
        if not result:
            return False # если неверно
        else:
            self.FIO = result[2]
            self.role = result[3]
            return True # если верно


class System():
    def __init__(self):
        self.numX = 0
        self.table = []
        self.autorized = False
        self.user:User = None

        self.title = ""
        self.ui = "+"
        self.uiX = "-"
        self.uiY = "|"
        self.row_max = 30
        self.rows = 3

    def changeSelector(self, num=0):
        if len(self.table[0])<0:
            return
        
        self.numX+=num
        if self.numX >= len(self.table[0])+1:
            self.numX = 0
        elif self.numX<0:
            self.numX = len(self.table[0])
        
    def printTable(self):
        system.printTitle()
        varPrint = ""
        for k in range(len(self.table)):
            for i in range(len(self.table[k][1])):
                varPrint+=f"{self.uiY}"
                if i==self.numX:
                    varPrint+="* "
                varPrint+=self.table[k][1][i]+"\n"
            print(varPrint)

    def printTitle(self):
        title0 = []
        for i in range(len(self.table)):
            title0.append(self.table[i][0])

        self.rows = len(title0)
        print(f"{self.ui}{self.uiX*(self.row_max//self.rows)}{self.ui}")
        print(f"{self.uiY}{self.title}{" "*10}{self.ui}")
        print(f"{self.ui}{self.uiX*(self.row_max//self.rows)}{self.ui}")

        # {self.user.get_name(0)}


    def getBase(self):
        pass

    def create_table(self):
        self.table = [
            ["Товары1", [
                "meow1",
                "товар ещё",
                "твоавоав"
            ]]
        ]

system = System()

user = system.user = User()

skipauto = False

while user.check()==False: # Проверка правильные ли данные
    if skipauto: # debug
        user.login = "yzls62@outlook.com"
        user.password = "JlFRCZ"
    else:
        print("Войти как гость нужно написать Гость")
        user.login = input("Login: ")
        if user.login!="Гость":
            user.password = input("Password: ")

    if user.check() or user.login == "Гость":
        system.autorized = True
        system.create_table()
        system.title = "Товары"
        system.printTable()
        break
    else:
        print("Неверные данные Х")

while system.autorized:
    match keyboard.read_key().lower():
        case "w":
            system.changeSelector(-1)
        case "s":
            system.changeSelector(1)
        case "ц":
            system.changeSelector(-1)
        case "ы":
            system.changeSelector(1)
    system.printTable()
    time.sleep(0.25)

    # через СУБД заполнение по ячейкам сделать ! !!!!!