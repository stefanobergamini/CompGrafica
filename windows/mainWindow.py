import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from models.button import Button

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 1000, 500)
        self.w = None  # No external window yet.
        self.btn1 = Button(self)
        self.btn1.mountButton("cima", 35, 0, 70, 50)

        self.btn2 = Button(self)
        self.btn2.mountButton("esquerda", 0, 50, 70, 50)

        self.btn3 = Button(self)
        self.btn3.mountButton("direita", 70, 50, 70, 50)

        self.btn4 = Button(self)
        self.btn4.mountButton("baixo", 35, 100, 70, 50)

        self.btn5 = Button(self)
        self.btn5.clicked.connect(self.show_new_window)
        self.btn5.mountButton(0, 150, 140, 50)

        self.buttonZoomOut = Button(self)
        self.buttonZoomOut.mountButton("-", 0, 200, 70, 50)

        self.buttonZoomIn = Button(self)
        self.buttonZoomIn.mountButton("+", 70, 200, 70, 50)


    def show_new_window(self, checked):
        if self.w is None:
            self.w = AnotherWindow()
        self.w.show()



