import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPalette, QImage, QBrush
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        WID, HEI = 800, 600
        self.setGeometry(300, 300, WID, HEI)
        self.setWindowTitle("Water counter")

        self.label = QLabel("Введите параметры:", self)
        self.label.move(15, 20)  # label Введите данные.

        self.lable1 = QLabel("ФИО:", self)
        self.lable1.move(15, 55)  # 1 label

        self.line1 = QLineEdit("", self)
        self.line1.resize(200, 25)
        self.line1.move(70, 50)  # Окно 1

        self.lable2 = QLabel("Возраст:", self)
        self.lable2.move(15, 90)  # 2 label

        self.line2 = QLineEdit("", self)
        self.line2.resize(200, 25)
        self.line2.move(70, 85)  # Окно 2

        self.lable3 = QLabel("Вес:", self)
        self.lable3.move(15, 125)  # 3 label

        self.line3 = QLineEdit("", self)
        self.line3.resize(200, 25)
        self.line3.move(70, 120)  # Окно 3

        self.lable4 = QLabel("Рост:", self)
        self.lable4.move(15, 160)  # 4 label

        self.line4 = QLineEdit("", self)
        self.line4.resize(200, 25)
        self.line4.move(70, 155)  # Окно 4

        self.btn = QPushButton('Начать расчёт', self)
        self.btn.resize(200, 50)
        self.btn.move(300, 400)  # Кнопка

        oImage = QImage("fon1.jpg")
        sImage = oImage.scaled(QSize(800, 600))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)  # Фон

        self.btn.clicked.connect(self.run)

    def run(self):
        self.w2 = WorkWindow()
        self.w2.show()
        self.hide()


class WorkWindow(Example):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        WID, HEI = 800, 600
        self.setGeometry(300, 300, WID, HEI)
        self.setWindowTitle("Water counter")

        oImage = QImage("fon1.jpg")
        sImage = oImage.scaled(QSize(800, 600))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)  # фон

        self.btn1 = QPushButton('+ 100 мл.', self)
        self.btn1.resize(150, 50)
        self.btn1.move(500, 90)  # + 0.1л.

        self.btn1 = QPushButton('+ 250 мл.', self)
        self.btn1.resize(150, 50)
        self.btn1.move(500, 150)  # + 0,25л.

        self.btn2 = QPushButton('+ 500 мл.', self)
        self.btn2.resize(150, 50)
        self.btn2.move(500, 210)  # + 0,5л.

        self.btn3 = QPushButton('+ 1 л.', self)
        self.btn3.resize(150, 50)
        self.btn3.move(500, 270)  # + 1л.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
