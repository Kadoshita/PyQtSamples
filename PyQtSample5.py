#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import datetime

class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):               
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('LineEdit')    

        self.textbox = QLineEdit(self)
        self.textbox.move(10,10)
        self.textbox.resize(140,20)
        self.show()

        timer = QTimer(self)
        timer.timeout.connect(self.time_draw)
        timer.start(1000) #msec       

    def time_draw(self):
        d = datetime.datetime.today()
        daystr=d.strftime("%Y-%m-%d %H:%M:%S")
        self.statusBar().showMessage(daystr)
        self.textbox.setText(daystr)

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()