import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

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
        btn1 = QPushButton("cima", self)
        #btn1.setText("texto dentro do botao")
        #btn1.move(200,200)
        btn1.setGeometry(35, 0, 70, 50)

        btn2 = QPushButton("esquerda", self)
        btn2.setGeometry(0, 50, 70, 50)

        btn3 = QPushButton("direita", self)
        btn3.setGeometry(70, 50, 70, 50)

        btn4 = QPushButton("baixo", self)
        btn4.setGeometry(35, 100, 70, 50)

        btn5 = QPushButton("inserir ponto/linha/linhas", self)
        btn5.setGeometry(0, 150, 140, 50)

        #self.show()


app = QApplication(sys.argv)
window = WindowOne()
window.show()
sys.exit(app.exec_())

app.exec_()
