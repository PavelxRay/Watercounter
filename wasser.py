import sys
from PyQt5 import uic
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush
import sqlite3


class FirstForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('parametrs.ui', self)
        self.start.clicked.connect(self.run)

    def run(self):
        second_form = SecondForm(self, weight1=self.weight1)
        second_form.show()
        self.hide()


class SecondForm(QMainWindow):
    def __init__(self, *args, weight1):
        super().__init__(*args)
        self.weight1 = weight1
        ves = int(self.weight1.text())
        con = sqlite3.connect("voda.db")
        cur = con.cursor()
        self.result = cur.execute(f"""SELECT Norma FROM Wasser
        WHERE Weight = {ves}""").fetchone()[0]
        self.initUI()

    def initUI(self):
        uic.loadUi('water.ui', self)
        # фон ко второму окну другим способом
        oImage = QImage("fon1.jpg")
        sImage = oImage.scaled(QSize(800, 600))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        #  фото создателя
        foto = QPixmap('itachi.jpg')
        self.label_4.setPixmap(foto)
        #  лейбл с выводом нормы учитывая параметры
        self.label_2.setText(f"{self.result}л.")
        # Кнопки
        self.oneoo.clicked.connect(self.main1)
        self.twofiveo.clicked.connect(self.main2)
        self.fiveoo.clicked.connect(self.main3)
        self.litre.clicked.connect(self.main4)
        #  выпитая вода
        self.a = 0
        # Дневник
        self.dn.clicked.connect(self.data)

        self.oneoo.setCheckable(True)
        self.twofiveo.setCheckable(True)
        self.fiveoo.setCheckable(True)
        self.litre.setCheckable(True)

    def main1(self):

        f1 = QPixmap('stakan1.png')
        f2 = QPixmap('stakan2.png')
        f3 = QPixmap('stakan3.png')
        f4 = QPixmap('stakan4.png')

        if self.oneoo.isChecked():
            self.a += 100
            self.oneoo.setChecked(False)

        if self.a < float(self.result) * 250:
            self.bottle.setPixmap(f1)

        elif float(self.result) * 250 <= self.a < float(self.result) * 500:
            self.bottle.setPixmap(f2)

        elif float(self.result) * 500 <= self.a < float(self.result) * 750:
            self.bottle.setPixmap(f2)

        elif float(self.result) * 750 <= self.a < float(self.result) * 1000:
            self.bottle.setPixmap(f3)

        elif self.a >= float(self.result) * 1000:
            self.bottle.setPixmap(f4)

    def main2(self):

        f1 = QPixmap('stakan1.png')
        f2 = QPixmap('stakan2.png')
        f3 = QPixmap('stakan3.png')
        f4 = QPixmap('stakan4.png')

        if self.twofiveo.isChecked():
            self.a += 250
            self.twofiveo.setChecked(False)

        if self.a < float(self.result) * 250:
            self.bottle.setPixmap(f1)

        elif float(self.result) * 250 <= self.a < float(self.result) * 500:
            self.bottle.setPixmap(f2)

        elif float(self.result) * 500 <= self.a < float(self.result) * 750:
            self.bottle.setPixmap(f2)

        elif float(self.result) * 750 <= self.a < float(self.result) * 1000:
            self.bottle.setPixmap(f3)

        elif self.a >= float(self.result) * 1000:
            self.bottle.setPixmap(f4)

    def main3(self):

        f1 = QPixmap('stakan1.png')
        f2 = QPixmap('stakan2.png')
        f3 = QPixmap('stakan3.png')
        f4 = QPixmap('stakan4.png')

        if self.fiveoo.isChecked():
            self.a += 500
            self.fiveoo.setChecked(False)

        if self.a < float(self.result) * 250:
            self.bottle.setPixmap(f1)

        elif float(self.result) * 250 <= self.a < float(self.result) * 500:
            self.bottle.setPixmap(f2)

        elif float(self.result) * 500 <= self.a < float(self.result) * 750:
            self.bottle.setPixmap(f2)

        elif float(self.result) * 750 <= self.a < float(self.result) * 1000:
            self.bottle.setPixmap(f3)

        elif self.a >= float(self.result) * 1000:
            self.bottle.setPixmap(f4)

    def main4(self):

        f1 = QPixmap('stakan1.png')
        f2 = QPixmap('stakan2.png')
        f3 = QPixmap('stakan3.png')
        f4 = QPixmap('stakan4.png')

        if self.litre.isChecked():
            self.a += 1000
            self.litre.setChecked(False)

        if self.a < float(self.result) * 250:
            self.bottle.setPixmap(f1)

        elif float(self.result) * 250 <= self.a < float(self.result) * 500:
            self.bottle.setPixmap(f2)

        elif float(self.result) * 500 <= self.a < float(self.result) * 750:
            self.bottle.setPixmap(f2)

        elif float(self.result) * 750 <= self.a < float(self.result) * 1000:
            self.bottle.setPixmap(f3)

        elif self.a >= float(self.result) * 1000:
            self.bottle.setPixmap(f4)

    def data(self):
        with open('dnevnik.txt', 'a', encoding='utf8') as f:
            f.write(f"Вы выпили {self.a / 1000}л. воды.\n")
            f.write("------------------------------------\n")


app = QApplication(sys.argv)
ex = FirstForm()
ex.show()
sys.exit(app.exec())
