#pyuic5 mainwindow.ui -o mainwindow.py

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("mainwindow.ui", self)
        self.pushButton.clicked.connect(self.click)
        
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
        
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
