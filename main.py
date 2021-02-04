import sys
from PyQt5.QtWidgets import QApplication, QWidget
from models.button import Button

class WindowOne(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("Trabalho 1")
        #self.setStyleSheet('background-color: black')
        self.create_buttons()

        #self.setFixedHeight(500)
        #self.setFixedWidth(500)

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

        self.show()


app = QApplication(sys.argv)
window = WindowOne()
window.show()
sys.exit(app.exec_())

app.exec_()
