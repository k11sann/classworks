#pyuic5 mainwindow.ui -o mainwindow.py
#pyuic5 lab1/mainwindow.ui -o lab1/mainwindow.py
#pyuic5 lab4/mainwindow.ui -o lab4/mainwindow.py

import sys, os, datetime, openpyxl, json, requests
from bs4 import BeautifulSoup
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QTableWidgetItem

from docxtpl import DocxTemplate
            
class MainClass(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("title/mainwindow.ui", self)
        self.setWindowTitle('Главная')
        
        self.infoBut.clicked.connect(self.displayMessageBox)
        
        self.lab1but.clicked.connect(self.lab1)
        self.lab2but.clicked.connect(self.lab2)
        self.lab3but.clicked.connect(self.lab3)
        self.lab4but.clicked.connect(self.lab4)
        self.lab5but.clicked.connect(self.lab5)
        #self.lab6but.clicked.connect(self.lab6)
        #self.lab7but.clicked.connect(self.lab7)
        #self.lab8but.clicked.connect(self.lab8)
        #self.lab9but.clicked.connect(self.lab9)
        #self.lab10but.clicked.connect(self.lab10)
        
    def displayMessageBox(self):
        QMessageBox.about(self, self.name.text(), "Имя: Даниэль\nФамилия: Субботин\nОтчество: Александрович\nГод рождения: 2006")
            
        
    def lab1(self):
        self.close()
        self.main = Lab1()
        self.main.show()
        
    def lab2(self):
        self.close()
        self.main = Lab2()
        self.main.show()

    def lab3(self):
        self.close()
        self.main = Lab3()
        self.main.show()
    
    def lab4(self):
        self.close()
        self.main = Lab4()
        self.main.show()
        
    def lab5(self):
        self.close()
        self.main = Lab5()
        self.main.show()
        
class Lab1(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("lab1/mainwindow.ui", self)
        self.pushButton.clicked.connect(self.click)
        self.backButton.clicked.connect(self.back)
        self.setWindowTitle('Лабораторная работа 1')
        
    def click(self):
        res = 0
        res1 = 0
        res2 = 0
        res3 = 0
        
        try:
            res1 = int(self.speed.toMarkdown()) + int(self.run.toMarkdown()) + int(self.swim.toMarkdown())
        except ValueError:
            res1=0    
        try:
            res2 = int(self.speed_2.toMarkdown()) + int(self.run_2.toMarkdown()) + int(self.swim_2.toMarkdown()) 
        except ValueError:
            res2=0
        try:
            res3 = int(self.speed_3.toMarkdown()) + int(self.run_3.toMarkdown()) + int(self.swim_3.toMarkdown()) 
        except ValueError:
            res3=0
                
        names = {
            res1:self.name.text(),
            res2:self.name_2.text(),
            res3:self.name_3.text(),
        }
            
        self.res.setText(str(res1))
        self.res_2.setText(str(res2))
        self.res_3.setText(str(res3))
        
        if res1==res2 or res2==res3 or res1==res3:
            self.label_6.setText("Найдены одинаковые результаты")
        else:
            res = max(res1,res2,res3)
            self.label_6.setText(str(names.pop(res)))
            
    def back(self):
        self.close()
        self.main = MainClass()
        self.main.show()
       
class Lab2(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("lab2/mainwindow.ui", self)
        self.buttonBox.accepted.connect(self.click)
        self.backBut.clicked.connect(self.back)
        self.setWindowTitle('Лабораторная работа 2')
        
    def click(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Открыть файл', '', '')
        
        self.pathEdit.setText(str(file_name))
            
        try:
            stat_info = os.stat(file_name)

            metadata = {
                'Имя файла': os.path.basename(file_name),
                'Тип': os.path.splitext(file_name)[1],
                'Дата создания': datetime.datetime.fromtimestamp(stat_info.st_ctime).strftime('%Y-%m-%d %H:%M:%S'),
                'Дата изменения': datetime.datetime.fromtimestamp(stat_info.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
                'Размер': stat_info.st_size,
                #'owner': pwd.getpwuid(stat_info.st_uid).pw_name
            }
            if metadata:
                self.infoLabel.setText("")
                for key, value in metadata.items():
                    self.infoLabel.setText(self.infoLabel.text()+f"\n{key}: {value}")
            else:
                self.infoLabel.setText("Ошибка при загрузке")          
            
        except:
            self.infoLabel.setText("Ошибка при загрузке")   
            
    def back(self):
        self.close()
        self.main = MainClass()
        self.main.show()
        
class Lab3(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("lab3/mainwindow.ui", self)
        self.exampleButton.accepted.connect(self.example)
        self.excelButton.accepted.connect(self.excel)
        self.saveButton.accepted.connect(self.save)
        self.resultBut.clicked.connect(self.result)
        self.backBut.clicked.connect(self.back)
        self.setWindowTitle('Лабораторная работа 3')

        self.example_path = ""
        self.excel_path = ""
        self.save_path = ""
        
    def example(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Открыть файл', '', '')
        
        self.examplePath.setText(str(file_name))
        self.example_path = str(file_name)

    def excel(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Выбрать файл', '', '')
        
        self.excelPath.setText(str(file_name))
        self.excel_path = str(file_name)

    def save(self):
        file_name = QFileDialog.getExistingDirectory(self, 'Выберите папку', '')
        
        self.savePath.setText(str(file_name))
        self.save_path = str(file_name)

    def result(self):
        if self.example_path != "" and self.excel_path!="" and self.save_path!="":
            print(self.example_path)
            print(self.excel_path)
            print(self.save_path)
            wb = openpyxl.load_workbook(self.excel_path)
            ws = wb.active
            data = []
            for row in ws.iter_rows(min_row=2):
                data.append({
                    'name': row[0].value,
                    'reason': row[1].value,
                    'chill_time': row[2].value
                })

            print(data)
            template = DocxTemplate(self.example_path)
            for i, record in enumerate(data):
                template.render(record)
                filename = f'{self.save_path}/result_{i + 1}.docx'
                template.save(filename)
            self.labelResult.setText("Успешно!")
        else:
            self.labelResult.setText("Не везде указан путь")
            if self.example_path=="":
                self.examplePath.setText("Путь не указан")
            if self.excel_path=="":
                self.excelPath.setText("Путь не указан")
            if self.save_path=="":
                self.savePath.setText("Путь не указан")

    def back(self):
        self.close()
        self.main = MainClass()
        self.main.show()
        
class Lab4(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("lab4/mainwindow.ui", self)
        self.resultBut.clicked.connect(self.example)
        self.backBut.clicked.connect(self.back)
        self.setWindowTitle('Лабораторная работа 4')
        
    def example(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Открыть файл', '', '')
        
        if file_name:
            self.labelResult.setText(str(file_name))
            jsondata = open(file_name).read()
            json_object = json.loads(jsondata)
            imdata = json_object["imdata"]
            
            data_list=["dn", "descr", "speed", "mtu"]
            
            self.tableWidget.setRowCount(len(imdata))
            self.tableWidget.setColumnCount(len(data_list))
            
            for i in imdata:
                for j in data_list:
                    info = i["l1PhysIf"]["attributes"][j]
                    self.tableWidget.setItem(int(imdata.index(i)), int(data_list.index(j)), QTableWidgetItem(info))
        else:
            self.labelResult.setText("Файл не выбран/Не найден")

    def back(self):
        self.close()
        self.main = MainClass()
        self.main.show()

class Lab5(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("lab4/mainwindow.ui", self)
        self.resultBut.clicked.connect(self.example)
        self.backBut.clicked.connect(self.back)
        self.setWindowTitle('Лабораторная работа 5')
        
    def example(self):
        url = 'https://minecraft-inside.ru/skins/'
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        nickname = soup.find_all('h2', class_='box__title')
        views = soup.find_all('div', class_='info__item post__views')

        self.labelResult.setText(str(url))

        self.tableWidget.setRowCount(len(nickname))
        self.tableWidget.setColumnCount(2)
        
        self.tableWidget.setItem(0, 0, QTableWidgetItem("Nickname"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Просмотры"))
        
        if r.status_code == 200:
            for i in range(0,len(nickname)):
                self.tableWidget.setItem(i+1, 0, QTableWidgetItem(str(nickname[i].text)))
                self.tableWidget.setItem(i+1, 1, QTableWidgetItem(str(views[i].text)))
        else:
            self.labelResult.setText("Ошибка : "+str(r.status_code))

    def back(self):
        self.close()
        self.main = MainClass()
        self.main.show()

app = QtWidgets.QApplication(sys.argv)
main = MainClass()
main.show()
app.exec()
