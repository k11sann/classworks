import sys
sys.path.insert(0, r'C:\Users\PYst\Desktop\meow\lab1')


from PyQt5 import QtCore, QtGui, QtWidgets, uic

from Truatlon import Lab1



class Title(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("title/mainwindow.ui", self)
        self.setWindowTitle('Главная')
        
        self.lab1but.clicked.connect(self.lab1)
        #self.lab2but.clicked.connect(self.lab2)
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