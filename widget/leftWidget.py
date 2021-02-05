from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QWidget
from widget.coordinatesWidget import CoordinatesWidget


class LeftWidget(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 200, 500)
        self.w = None  # No external window yet.
        self.btn1 = QPushButton("cima", self)
        self.btn1.setGeometry(35, 0, 70, 50)

        self.btn2 = QPushButton("esquerda", self)
        self.btn2.setGeometry(0, 50, 70, 50)

        self.btn3 = QPushButton("direita", self)
        self.btn3.setGeometry(70, 50, 70, 50)

        self.btn4 = QPushButton("baixo", self)
        self.btn4.setGeometry(35, 100, 70, 50)

        self.btn5 = QPushButton("inserir ponto/linha/linhas", self)
        self.btn5.clicked.connect(self.show_new_window)
        self.btn5.setGeometry(0, 150, 140, 50)
       
    def show_new_window(self, checked):
        if self.w is None:
            self.w = CoordinatesWidget()
        self.w.show()
