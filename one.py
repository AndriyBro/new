import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ddd.ui',self)
        self.dolar.clicked.connect(self.dollars)
        self.pushButton_6.clicked.connect(self.dorivnue)
        self.euro.clicked.connect(self.euro1)


    def dollars(self):
        with open('curs.txt', 'r') as f:
            nums = f.read().splitlines()
        curs_dollar = nums[0]
        self.curs.setText(curs_dollar)
    def euro1(self):
        with open('curs.txt', 'r') as f:
            nums = f.read().splitlines()
        curs_euro = nums[1]
        self.curs.setText(curs_euro)

    def dorivnue(self):
        a = float(self.curs.text())
        b= float(self.Pole.text())
        self.Pole.setText(str(a*b))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())