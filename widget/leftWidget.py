from PyQt5.QtWidgets import QPushButton, QWidget
from widget.coordinatesWidgetPonto import CoordinatesWidgetPonto
from widget.coordinatesWidgetLinha import CoordinatesWidgetLinha
from widget.coordinatesWidgetPoligono import CoordinatesWidgetPoligono
from windows.window import Window


class LeftWidget(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        self.coordinatesWidgetLinha = None  # No external window yet.
        self.coordinatesWidgetPonto = None  # No external window yet.
        self.coordinatesWidgetPoligono = None  # No external window yet.
        self.btn1 = QPushButton("Up", self)
        self.btn1.clicked.connect(Window.moveUp)
        self.btn1.setGeometry(43, 30, 86, 25)

        self.btn2 = QPushButton("Left", self)
        self.btn2.clicked.connect(Window.moveLeft)
        self.btn2.setGeometry(0, 55, 86, 25)

        self.btn3 = QPushButton("Right", self)
        self.btn3.clicked.connect(Window.moveRight)
        self.btn3.setGeometry(86, 55, 86, 25)

        self.btn4 = QPushButton("Down", self)
        self.btn4.clicked.connect(Window.moveDown)
        self.btn4.setGeometry(43, 80, 86, 25)

        self.btn5 = QPushButton("Insert Point", self)
        self.btn5.clicked.connect(self.show_new_window_ponto)
        self.btn5.setGeometry(0, 215, 173, 25)

        self.btn6 = QPushButton("Insert Line", self)
        self.btn6.clicked.connect(self.show_new_window_linha)
        self.btn6.setGeometry(0, 240, 173, 25)

        self.btn7 = QPushButton("Insert Poligon", self)
        self.btn7.clicked.connect(self.show_new_window_poligono)
        self.btn7.setGeometry(0, 265, 173, 25)

        self.btn8 = QPushButton("Zoom In", self)
        self.btn8.clicked.connect(Window.zoomIn)
        self.btn8.setGeometry(0, 125, 86, 25)

        self.btn9 = QPushButton("Zoom Out", self)
        self.btn9.clicked.connect(Window.zoomOut)
        self.btn9.setGeometry(86, 125, 86, 25)

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
