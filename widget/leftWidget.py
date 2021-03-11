from PyQt5.QtWidgets import QPushButton, QWidget, QCheckBox, QButtonGroup
from widget.coordinatesWidgetPonto import CoordinatesWidgetPonto
from widget.coordinatesWidgetLinha import CoordinatesWidgetLinha
from widget.coordinatesWidgetPoligono import CoordinatesWidgetPoligono

from models.window import Window


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
        self.buttonUp.clicked.connect(self.moveUp)
        self.buttonUp.setGeometry(43, 30, 86, 25)

        self.buttonLeft = QPushButton("Left", self)
        self.buttonLeft.clicked.connect(self.moveLeft)
        self.buttonLeft.setGeometry(0, 55, 86, 25)

        self.buttonRight = QPushButton("Right", self)
        self.buttonRight.clicked.connect(self.moveRight)
        self.buttonRight.setGeometry(86, 55, 86, 25)

        self.buttonDown = QPushButton("Down", self)
        self.buttonDown.clicked.connect(self.moveDown)
        self.buttonDown.setGeometry(43, 80, 86, 25)

        self.buttonZoomIn = QPushButton("Zoom In", self)
        self.buttonZoomIn.clicked.connect(self.zoomIn)
        self.buttonZoomIn.setGeometry(0, 125, 86, 25)

        self.buttonZoomOut = QPushButton("Zoom Out", self)
        self.buttonZoomOut.clicked.connect(self.zoomOut)
        self.buttonZoomOut.setGeometry(86, 125, 86, 25)

        self.buttonRotateLeft = QPushButton("Rotate Window Left", self)
        self.buttonRotateLeft.clicked.connect(self.rotateLeft)
        self.buttonRotateLeft.setGeometry(0, 165, 173, 25)

        self.buttonRotateRight = QPushButton("Rotate Window Right", self)
        self.buttonRotateRight.clicked.connect(self.rotateRight)
        self.buttonRotateRight.setGeometry(0, 190, 173, 25)

        self.buttonPoint = QPushButton("Insert Point", self)
        self.buttonPoint.clicked.connect(self.show_new_window_ponto)
        self.buttonPoint.setGeometry(0, 230, 173, 25)

        self.buttonLine = QPushButton("Insert Line", self)
        self.buttonLine.clicked.connect(self.show_new_window_linha)
        self.buttonLine.setGeometry(0, 255, 173, 25)

        self.buttonPolygon = QPushButton("Insert Poligon", self)
        self.buttonPolygon.clicked.connect(self.show_new_window_poligono)
        self.buttonPolygon.setGeometry(0, 280, 173, 25)

        self.checkBox1 = QCheckBox("Tecnica 1", self)
        self.checkBox1.setChecked(True)
        self.checkBox1.stateChanged.connect(lambda: self.chosenTecnic(self.checkBox1))
        self.checkBox1.setGeometry(0, 305, 86, 25)

        self.checkBox2 = QCheckBox("Tecnica 2", self)
        self.checkBox1.stateChanged.connect(lambda: self.chosenTecnic(self.checkBox2))
        self.checkBox2.setGeometry(86, 305, 86, 25)

        self.bg = QButtonGroup()
        self.bg.addButton(self.checkBox1, 1)
        self.bg.addButton(self.checkBox2, 2)

    def show_new_window_ponto(self):
        if self.coordinatesWidgetPonto is None:
            self.coordinatesWidgetPonto = CoordinatesWidgetPonto()
        self.coordinatesWidgetPonto.show()

    def show_new_window_linha(self):
        if self.coordinatesWidgetLinha is None:
            self.coordinatesWidgetLinha = CoordinatesWidgetLinha()
        self.coordinatesWidgetLinha.show()

    def show_new_window_poligono(self):
        if self.coordinatesWidgetPoligono is None:
            self.coordinatesWidgetPoligono = CoordinatesWidgetPoligono()
        self.coordinatesWidgetPoligono.show()

    def rotateRight(self):
        Window.rotateWindow(-10)

    def rotateLeft(self):
        Window.rotateWindow(10)

    def moveUp(self):
        Window.move([0, 5])

    def moveDown(self):
        Window.move([0, -5])

    def moveLeft(self):
        Window.move([-5, 0])

    def moveRight(self):
        Window.move([5, 0])

    def zoomIn(self):
        Window.zoom(0.9)

    def zoomOut(self):
        Window.zoom(1.1)

    def chosenTecnic(self, checkBox):
        if checkBox.text() == "Tecnica 1":
            if checkBox.isChecked() == True:
                print(checkBox.text() + " is selected")
            else:
                print(checkBox.text() + " is deselected")

        if checkBox.text() == "Tecnica 2":
            if checkBox.isChecked() == True:
                print(checkBox.text() + " is selected")
            else:
                print(checkBox.text() + " is deselected")