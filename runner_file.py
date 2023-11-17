from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QWidget
from random import choice

app = QApplication([])


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.flag = True
        self.hammasi = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.xlar = []
        self.nollar = []
        self.win_conditions = [ [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8],  [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        gr = QGridLayout()
        self.btns = []
        for i in range(1, 10):
            self.btns.append(QPushButton(""))

        reset_btn = QPushButton("RESET ♻️")
        reset_btn.setFixedSize(200, 100)
        cnt = 0
        for i in self.btns:
            cnt += 1
            i.setFixedSize(200, 200)
            i.setStyleSheet("background-color: white")
            font = QFont()
            font.setPointSize(50)
            i.setText("")
            i.setFont(font)
            i.setObjectName(f"{cnt}")
            i.clicked.connect(self.button_clicked_2)
        reset_btn.clicked.connect(self.reset_clicked)
        gr.addWidget(reset_btn, 3, 1)
        cnt = 0
        for i in range(3):
            for j in range(3):
                gr.addWidget(self.btns[cnt], i, j)
                cnt += 1
        widg = QWidget()
        widg.setLayout(gr)
        self.setCentralWidget(widg)

    def button_clicked(self):
        index = int(self.sender().objectName())
        if self.flag:
            self.sender().setText("X")
            self.xlar.append(index)
        else:
            self.sender().setText("0")
            self.nollar.append(index)
        self.hammasi.remove(index)
        self.check_win()
        self.sender().setEnabled(False)
        self.toggle()

    def button_clicked_2(self):
        index = int(self.sender().objectName())
        self.hammasi.remove(index)
        self.sender().setText("X")
        self.sender().setEnabled(False)
        self.xlar.append(index)
        self.check_win()
        self.bot_bosdi()

    def bot_bosdi(self):
        if len(self.hammasi):
            a = choice(self.hammasi)
            self.btns[a - 1].setText("0")
            self.nollar.append(a)
            self.hammasi.remove(a)
            self.check_win()
            self.btns[a - 1].setEnabled(False)
            self.toggle()

    def reset_clicked(self):
        for i in self.btns:
            i.setText("")
            self.xlar = []
            self.nollar = []
            i.setEnabled(True)
            i.setStyleSheet("background-color: white")
            self.hammasi = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.flag = True

    def check_win(self):
        for i in self.win_conditions:
            if set(i).issubset(set(self.xlar)) or \
                    set(i).issubset(self.nollar):
                for c in i:
                    self.findChild(QPushButton, str(c)).setStyleSheet("background-color:green")
                for j in self.btns:
                    j.setEnabled(False)

    def toggle(self):
        self.flag = not self.flag


if __name__ == "__main__":
    a = MainWindow()
    a.show()
    app.exec()
