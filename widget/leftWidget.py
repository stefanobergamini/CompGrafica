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
        self.buttonUp = QPushButton("Up", self)
        self.buttonUp.clicked.connect(Window.moveUp)
        self.buttonUp.setGeometry(43, 30, 86, 25)

        self.buttonLeft = QPushButton("Left", self)
        self.buttonLeft.clicked.connect(Window.moveLeft)
        self.buttonLeft.setGeometry(0, 55, 86, 25)

        self.buttonRight = QPushButton("Right", self)
        self.buttonRight.clicked.connect(Window.moveRight)
        self.buttonRight.setGeometry(86, 55, 86, 25)

        self.buttonDown = QPushButton("Down", self)
        self.buttonDown.clicked.connect(Window.moveDown)
        self.buttonDown.setGeometry(43, 80, 86, 25)

        self.buttonPoint = QPushButton("Insert Point", self)
        self.buttonPoint.clicked.connect(self.show_new_window_ponto)
        self.buttonPoint.setGeometry(0, 215, 173, 25)

        self.buttonLine = QPushButton("Insert Line", self)
        self.buttonLine.clicked.connect(self.show_new_window_linha)
        self.buttonLine.setGeometry(0, 240, 173, 25)

        self.buttonPolygon = QPushButton("Insert Poligon", self)
        self.buttonPolygon.clicked.connect(self.show_new_window_poligono)
        self.buttonPolygon.setGeometry(0, 265, 173, 25)

        self.buttonZoomIn = QPushButton("Zoom In", self)
        self.buttonZoomIn.clicked.connect(Window.zoomIn)
        self.buttonZoomIn.setGeometry(0, 125, 86, 25)

        self.buttonZoomOut = QPushButton("Zoom Out", self)
        self.buttonZoomOut.clicked.connect(Window.zoomOut)
        self.buttonZoomOut.setGeometry(86, 125, 86, 25)

    def show_new_window_ponto(self):
        self.transformation = TransformationWidget()
        self.transformation.show()

    def show_new_window_linha(self):
        if self.coordinatesWidgetLinha is None:
            self.coordinatesWidgetLinha = CoordinatesWidgetLinha()
        self.coordinatesWidgetLinha.show()

    def show_new_window_poligono(self):
        if self.coordinatesWidgetPoligono is None:
            self.coordinatesWidgetPoligono = CoordinatesWidgetPoligono()
        self.coordinatesWidgetPoligono.show()
