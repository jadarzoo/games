import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget
from random import shuffle


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.btns = []
        self.btn_numbers = list(range(1, 16))
        shuffle(self.btn_numbers)
        self.btn_numbers.append(None)  # Adding None to represent the empty space

        for i in self.btn_numbers:
            if i is not None:
                self.btns.append(QPushButton(f"{i}"))
            else:
                self.btns.append(QPushButton(""))

        for i, btn in enumerate(self.btns):
            btn.setFixedSize(150, 150)
            btn.setStyleSheet("background-color: white")
            btn.setObjectName(str(i + 1) if i + 1 in self.btn_numbers[:-1] else "Empty")

            font = QFont()
            font.setPointSize(30)
            btn.setFont(font)

            # if i + 1 not in self.btn_numbers[:-1]:
            #     btn.setEnabled(False)

            btn.clicked.connect(self.buttonClicked)

        gr = QGridLayout()
        cnt = 0
        for i in range(4):
            for j in range(4):
                gr.addWidget(self.btns[cnt], i, j)
                cnt += 1

        widg = QWidget()
        widg.setLayout(gr)
        self.setCentralWidget(widg)

    def buttonClicked(self):
        sender_button = self.sender()
        empty_button = None

        for btn in self.btns:
            if btn.text() == "":
                empty_button = btn
                break

        if empty_button is not None and sender_button != empty_button:
            # Swap text and update object names
            sender_text = sender_button.text()
            sender_button.setText("")
            sender_button.setObjectName("Empty")

            empty_text = empty_button.text()
            empty_button.setText(sender_text)
            empty_button.setObjectName(sender_text)

            # sender_button.setEnabled(sender_text != "")
            # empty_button.setEnabled(empty_text != "")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wind = MainWindow()
    wind.show()
    sys.exit(app.exec_())
