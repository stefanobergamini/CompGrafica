import sys
from PyQt5.QtWidgets import QApplication, QWidget
from models.button import Button
from mainWindow import MainWindow

class Main():
    def __init__(self):
        app = QApplication(sys.argv)

        mainWindow = MainWindow()
        self.create_buttons(mainWindow)
        mainWindow.show()

        sys.exit(app.exec_())
        app.exec_()

    def create_buttons(self, parent):
        buttonCima = Button(parent)
        buttonCima.mountButton("cima", 35, 0, 70, 50)

        buttonEsquerda = Button(parent)
        buttonEsquerda.mountButton("esquerda", 0, 50, 70, 50)

        buttonDireita = Button(parent)
        buttonDireita.mountButton("direita", 70, 50, 70, 50)

        buttonBaixo = Button(parent)
        buttonBaixo.mountButton("baixo", 35, 100, 70, 50)

        buttonInserir = Button(parent)
        buttonInserir.mountButton("criar ponto/linha/poligonos", 0, 150, 140, 50)

        buttonZoomOut = Button(parent)
        buttonZoomOut.mountButton("-", 0, 200, 70, 50)

        buttonZoomIn = Button(parent)
        buttonZoomIn.mountButton("+", 70, 200, 70, 50)

Main()
