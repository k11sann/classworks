#pyuic5 mainwindow.ui -o mainwindow.py
#pyuic5 lab1/mainwindow.ui -o lab1/mainwindow.py

import sys, os, datetime
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog


      
            
class MainClass(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("title/mainwindow.ui", self)
        self.setWindowTitle('Главная')
        
        self.lab1but.clicked.connect(self.lab1)
        self.lab2but.clicked.connect(self.lab2)
        #self.lab3but.clicked.connect(self.lab3)
        #self.lab4but.clicked.connect(self.lab4)
        #self.lab5but.clicked.connect(self.lab5)
        #self.lab6but.clicked.connect(self.lab6)
        #self.lab7but.clicked.connect(self.lab7)
        #self.lab8but.clicked.connect(self.lab8)
        #self.lab9but.clicked.connect(self.lab9)
        #self.lab10but.clicked.connect(self.lab10)
        
    def lab1(self):
        self.close()
        self.main = Lab1()
        self.main.show()
        
    def lab2(self):
        self.close()
        self.main = Lab2()
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
        
app = QtWidgets.QApplication(sys.argv)
main = MainClass()
main.show()
app.exec()