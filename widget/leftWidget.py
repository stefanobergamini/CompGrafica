from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QWidget
from widget.coordinatesWidgetPonto import CoordinatesWidgetPonto
from widget.coordinatesWidgetLinha import CoordinatesWidgetLinha
from widget.coordinatesWidgetPoligono import CoordinatesWidgetPoligono


class LeftWidget(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 200, 500)
        self.coordinatesWidgetLinha = None  # No external window yet.
        self.coordinatesWidgetPonto = None  # No external window yet.
        self.coordinatesWidgetPoligono = None  # No external window yet.
        self.btn1 = QPushButton("cima", self)
        self.btn1.setGeometry(35, 0, 70, 50)

        self.btn2 = QPushButton("esquerda", self)
        self.btn2.setGeometry(0, 50, 70, 50)

        self.btn3 = QPushButton("direita", self)
        self.btn3.setGeometry(70, 50, 70, 50)

        self.btn4 = QPushButton("baixo", self)
        self.btn4.setGeometry(35, 100, 70, 50)

        self.btn5 = QPushButton("inserir ponto", self)
        self.btn5.clicked.connect(self.show_new_window_ponto)
        self.btn5.setGeometry(0, 150, 140, 50)

        self.btn6 = QPushButton("inserir linha", self)
        self.btn6.clicked.connect(self.show_new_window_linha)
        self.btn6.setGeometry(0, 200, 140, 50)

        self.btn7 = QPushButton("inserir poligono", self)
        self.btn7.clicked.connect(self.show_new_window_poligono)
        self.btn7.setGeometry(0, 250, 140, 50)

        self.btn8 = QPushButton("Zoom In", self)
        self.btn8.setGeometry(0, 300, 70, 50)

        self.btn9 = QPushButton("Zoom Out", self)
        self.btn9.setGeometry(70, 300, 70, 50)
       
    def show_new_window_ponto(self, checked):
        if self.coordinatesWidgetPonto is None:
            self.coordinatesWidgetPonto = CoordinatesWidgetPonto()
        self.coordinatesWidgetPonto.show()

    def show_new_window_linha(self, checked):
        if self.coordinatesWidgetLinha is None:
            self.coordinatesWidgetLinha = CoordinatesWidgetLinha()
        self.coordinatesWidgetLinha.show()

    def show_new_window_poligono(self, checked):
        if self.coordinatesWidgetPoligono is None:
            self.coordinatesWidgetPoligono = CoordinatesWidgetPoligono()
        self.coordinatesWidgetPoligono.show()
