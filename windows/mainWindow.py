import sys
from PyQt5.QtWidgets import QWidget, QApplication
from models.button import Button

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Trabalho 1')
        self.create_buttons()
        self.show()


    def create_buttons(self):
        buttonCima = Button(self)
        buttonCima.mountButton("cima", 35, 0, 70, 50)

        buttonEsquerda = Button(self)
        buttonEsquerda.mountButton("esquerda", 0, 50, 70, 50)

        buttonDireita = Button(self)
        buttonDireita.mountButton("direita", 70, 50, 70, 50)

        buttonBaixo = Button(self)
        buttonBaixo.mountButton("baixo", 35, 100, 70, 50)

        buttonInserir = Button(self)
        buttonInserir.mountButton("criar ponto/linha/poligonos", 0, 150, 140, 50)

        buttonZoomOut = Button(self)
        buttonZoomOut.mountButton("-", 0, 200, 70, 50)

        buttonZoomIn = Button(self)
        buttonZoomIn.mountButton("+", 70, 200, 70, 50)
