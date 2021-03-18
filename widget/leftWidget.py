from PyQt5.QtWidgets import QPushButton, QWidget, QCheckBox, QButtonGroup, QLabel, QLineEdit
from widget.coordinatesWidgetPonto import CoordinatesWidgetPonto
from widget.coordinatesWidgetLinha import CoordinatesWidgetLinha
from widget.coordinatesWidgetPoligono import CoordinatesWidgetPoligono
from widget.coordinatesWidgetCurve import CoordinatesWidgetCurve

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
        self.coordinatesWidgetCurve = None  # No external window yet.

        self.buttonUp = QPushButton("Up", self)
        self.buttonUp.clicked.connect(self.moveUp)
        self.buttonUp.setGeometry(43, 10, 86, 25)

        self.buttonLeft = QPushButton("Left", self)
        self.buttonLeft.clicked.connect(self.moveLeft)
        self.buttonLeft.setGeometry(0, 35, 86, 25)

        self.buttonRight = QPushButton("Right", self)
        self.buttonRight.clicked.connect(self.moveRight)
        self.buttonRight.setGeometry(86, 35, 86, 25)

        self.buttonDown = QPushButton("Down", self)
        self.buttonDown.clicked.connect(self.moveDown)
        self.buttonDown.setGeometry(43, 60, 86, 25)

        self.buttonZoomIn = QPushButton("Zoom In", self)
        self.buttonZoomIn.clicked.connect(self.zoomIn)
        self.buttonZoomIn.setGeometry(0, 90, 86, 25)

        self.buttonZoomOut = QPushButton("Zoom Out", self)
        self.buttonZoomOut.clicked.connect(self.zoomOut)
        self.buttonZoomOut.setGeometry(86, 90, 86, 25)

        self.rotateWinAngLabel = QLabel("Rotation Window Angle:", self)
        self.rotateWinAngLabel.setGeometry(0, 130, 120, 25)
        self.rotateWinAng = QLineEdit("10", self)
        self.rotateWinAng.setGeometry(120, 130, 52, 25)

        self.buttonRotateLeft = QPushButton("Rotate Window", self)
        self.buttonRotateLeft.clicked.connect(self.rotateWindow)
        self.buttonRotateLeft.setGeometry(0, 155, 173, 25)


        self.buttonPoint = QPushButton("Insert Point", self)
        self.buttonPoint.clicked.connect(self.show_new_window_ponto)
        self.buttonPoint.setGeometry(0, 220, 173, 25)

        self.buttonLine = QPushButton("Insert Line", self)
        self.buttonLine.clicked.connect(self.show_new_window_linha)
        self.buttonLine.setGeometry(0, 245, 173, 25)

        self.buttonPolygon = QPushButton("Insert Poligon", self)
        self.buttonPolygon.clicked.connect(self.show_new_window_poligono)
        self.buttonPolygon.setGeometry(0, 270, 173, 25)

        self.buttonCurve = QPushButton("Insert Curve", self)
        self.buttonCurve.clicked.connect(self.show_new_window_curve)
        self.buttonCurve.setGeometry(0, 295, 173, 25)

        self.checkBox1 = QCheckBox("Cohen-Sutherland", self)
        self.checkBox1.setChecked(True)
        self.checkBox1.stateChanged.connect(lambda: self.chosenTecnic(self.checkBox1))
        self.checkBox1.setGeometry(0, 320, 86, 25)

        self.checkBox2 = QCheckBox("Liang-Barsky", self)
        self.checkBox1.stateChanged.connect(lambda: self.chosenTecnic(self.checkBox2))
        self.checkBox2.setGeometry(86, 320, 86, 25)

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

    def show_new_window_curve(self):
        if self.coordinatesWidgetCurve is None:
            self.coordinatesWidgetCurve = CoordinatesWidgetCurve()
        self.coordinatesWidgetCurve.show()

    def rotateWindow(self):
        angleWin = int (self.rotateWinAng.displayText())
        Window.rotateWindow(angleWin)

    def moveUp(self):
        Window.move([0, 15])

    def moveDown(self):
        Window.move([0, -15])

    def moveLeft(self):
        Window.move([-15, 0])

    def moveRight(self):
        Window.move([15, 0])

    def zoomIn(self):
        Window.zoom(0.9)

    def zoomOut(self):
        Window.zoom(1.1)

    def chosenTecnic(self, checkBox):
        if checkBox.text() == "Cohen-Sutherland":
            if checkBox.isChecked() == True:
                Window.LINECLIPPING = "CohenSutherland"
        if checkBox.text() == "Liang-Barsky":
            if checkBox.isChecked() == True:
                Window.LINECLIPPING = "LiangBarsky"
