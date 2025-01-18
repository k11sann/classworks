import sys
import random
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

# pyuic5 project.ui -o Project.py

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.count=0
        uic.loadUi("project.ui", self)
        self.pushButton.clicked.connect(self.plus_click)
        
    def plus_click(self):
        self.count+=1
        self.label_3.setText(f"Кол-во нажатий : {self.count}")
        numX= random.randint(15, 215)
        numY= random.randint(75, 215)
        print("x = "+str(numX)+"y = "+str(numY))
        self.pushButton.setGeometry(QtCore.QRect(numX, numY, 75, 23))
        self.progressBar.setProperty("value", self.count*2)
        if self.count == 50:
            self.label.setText("Вы прошли игру!")
        print("meow")
        
    
        
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()