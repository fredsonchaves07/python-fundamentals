import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLineEdit, QSizePolicy


class Calc(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.display = QLineEdit()

        self.setWindowTitle("Calculator app")
        self.setFixedSize(400, 400)
        self.grid.addWidget(self.display, 0, 0, 1, 5) 
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            "* {background: #FFF; color: #000; font-size: 30px;}"
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.add_btn(QPushButton("7"), 1, 0, 1, 1)
        self.add_btn(QPushButton("8"), 1, 1, 1, 1)
        self.add_btn(QPushButton("9"), 1, 2, 1, 1)
        self.add_btn(QPushButton("+"), 1, 3, 1, 1)
        self.add_btn(QPushButton("C"), 1, 4, 1, 1, lambda: self.display.setText(""))
        self.add_btn(QPushButton("4"), 2, 0, 1, 1)
        self.add_btn(QPushButton("5"), 2, 1, 1, 1)
        self.add_btn(QPushButton("6"), 2, 2, 1, 1)
        self.add_btn(QPushButton("-"), 2, 3, 1, 1)
        self.add_btn(QPushButton("<-"), 2, 4, 1, 1, lambda: self.display.setText(self.display.text()[:-1]))
        self.add_btn(QPushButton("1"), 3, 0, 1, 1)
        self.add_btn(QPushButton("2"), 3, 1, 1, 1)
        self.add_btn(QPushButton("3"), 3, 2, 1, 1)
        self.add_btn(QPushButton("/"), 3, 3, 1, 1)
        self.add_btn(QPushButton(""), 3, 4, 1, 1)
        self.add_btn(QPushButton("."), 4, 0, 1, 1)
        self.add_btn(QPushButton("0"), 4, 1, 1, 1)
        self.add_btn(QPushButton(""), 4, 2, 1, 1)
        self.add_btn(QPushButton("*"), 4, 3, 1, 1)
        self.add_btn(QPushButton("="), 4, 4, 1, 1, self.eval_igual)

        self.setCentralWidget(self.cw)
    
    def add_btn(self, btn, row, col, rowspan, colspan, function=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        if not function:
            btn.clicked.connect(lambda: self.display.setText(self.display.text() + btn.text()))
        else:
            btn.clicked.connect(function)
        
        if style:
            btn.setStyleSheet(style)
    
    def eval_igual(self):
        try:
            self.display.setText(str(eval(self.display.text())))
        except Exception as error:
            self.display.setText("Conta invalida!")


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    calc = Calc()
    calc.show()
    qt.exec_()