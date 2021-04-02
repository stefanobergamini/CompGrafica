from PyQt5.QtWidgets import QPushButton, QWidget, QCheckBox, QButtonGroup, QLabel, QLineEdit, QFileDialog
from widget.coordinatesWidgetPonto import CoordinatesWidgetPonto
from widget.coordinatesWidgetLinha import CoordinatesWidgetLinha
from widget.coordinatesWidgetPoligono import CoordinatesWidgetPoligono
from widget.coordinatesWidgetCurve import CoordinatesWidgetCurve
from widget.coordinatesWidgetSpline import CoordinatesWidgetSpline
from widget.coordinatesWidgetObj3D import CoordinatesWidgetObj3D

from models.window import Window
from models.world import World
from models.object2D import Object2D


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
        self.coordinatesWidgetSpline = None  # No external window yet.
        self.coordinatesWidgetObj3D = None  # No external window yet.

        self.buttonUp = QPushButton("Up", self)
        self.buttonUp.clicked.connect(self.moveUp)
        self.buttonUp.setGeometry(43, 0, 86, 25)

        self.buttonLeft = QPushButton("Left", self)
        self.buttonLeft.clicked.connect(self.moveLeft)
        self.buttonLeft.setGeometry(0, 25, 86, 25)

        self.buttonRight = QPushButton("Right", self)
        self.buttonRight.clicked.connect(self.moveRight)
        self.buttonRight.setGeometry(86, 25, 86, 25)

        self.buttonDown = QPushButton("Down", self)
        self.buttonDown.clicked.connect(self.moveDown)
        self.buttonDown.setGeometry(43, 50, 86, 25)

        self.buttonZoomIn = QPushButton("-", self)
        self.buttonZoomIn.clicked.connect(self.zoomIn)
        self.buttonZoomIn.setGeometry(0, 62, 43, 25)

        self.buttonZoomOut = QPushButton("+", self)
        self.buttonZoomOut.clicked.connect(self.zoomOut)
        self.buttonZoomOut.setGeometry(129, 62, 43, 25)

        self.buttonUp = QPushButton("Look Up", self)
        self.buttonUp.clicked.connect(self.moveLookUp)
        self.buttonUp.setGeometry(43, 75, 86, 25)

        self.buttonLeft = QPushButton("Look Left", self)
        self.buttonLeft.clicked.connect(self.moveLookLeft)
        self.buttonLeft.setGeometry(0, 100, 86, 25)

        self.buttonRight = QPushButton("Look Right", self)
        self.buttonRight.clicked.connect(self.moveLookRight)
        self.buttonRight.setGeometry(86, 100, 86, 25)

        self.buttonDown = QPushButton("Look Down", self)
        self.buttonDown.clicked.connect(self.moveLookDown)
        self.buttonDown.setGeometry(43, 125, 86, 25)

        self.rotateWinAngLabel = QLabel("Rotation Window Angle:", self)
        self.rotateWinAngLabel.setGeometry(0, 150, 120, 25)
        self.rotateWinAng = QLineEdit("10", self)
        self.rotateWinAng.setGeometry(120, 150, 52, 25)

        self.buttonRotateLeft = QPushButton("Rotate Window", self)
        self.buttonRotateLeft.clicked.connect(self.rotateWindow)
        self.buttonRotateLeft.setGeometry(0, 175, 173, 25)

        self.insertLabel = QLabel("Insert:", self)
        self.insertLabel.setGeometry(0, 200, 120, 25)

        self.buttonPoint = QPushButton("Point", self)
        self.buttonPoint.clicked.connect(self.show_new_window_ponto)
        self.buttonPoint.setGeometry(0, 225, 58, 25)

        self.buttonLine = QPushButton("Line", self)
        self.buttonLine.clicked.connect(self.show_new_window_linha)
        self.buttonLine.setGeometry(57, 225, 59, 25)

        self.buttonPolygon = QPushButton("Poligon", self)
        self.buttonPolygon.clicked.connect(self.show_new_window_poligono)
        self.buttonPolygon.setGeometry(115, 225, 57, 25)

        self.buttonSpline = QPushButton("Spline", self)
        self.buttonSpline.clicked.connect(self.show_new_window_spline)
        self.buttonSpline.setGeometry(0, 250, 58, 25)

        self.buttonCurve = QPushButton("Curve", self)
        self.buttonCurve.clicked.connect(self.show_new_window_curve)
        self.buttonCurve.setGeometry(57, 250, 59, 25)

        self.buttonObj3D = QPushButton("Obj 3D", self)
        self.buttonObj3D.clicked.connect(self.show_new_window_obj3d)
        self.buttonObj3D.setGeometry(115, 250, 57, 25)

        self.checkBox1 = QCheckBox("Cohen-Sutherland", self)
        self.checkBox1.setChecked(True)
        self.checkBox1.stateChanged.connect(lambda: self.chosenTecnic(self.checkBox1))
        self.checkBox1.setGeometry(0, 285, 86, 25)

        self.checkBox2 = QCheckBox("Liang-Barsky", self)
        self.checkBox1.stateChanged.connect(lambda: self.chosenTecnic(self.checkBox2))
        self.checkBox2.setGeometry(86, 285, 86, 25)

        self.buttonImport = QPushButton("Import", self)
        self.buttonImport.clicked.connect(self.importObject)
        self.buttonImport.setGeometry(0, 315, 86, 25)

        self.buttonExport = QPushButton("Export", self)
        self.buttonExport.clicked.connect(self.exportObject)
        self.buttonExport.setGeometry(86, 315, 86, 25)

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

    def show_new_window_spline(self):
        if self.coordinatesWidgetSpline is None:
            self.coordinatesWidgetSpline = CoordinatesWidgetSpline()
        self.coordinatesWidgetSpline.show()

    def show_new_window_obj3d(self):
        if self.coordinatesWidgetObj3D is None:
            self.coordinatesWidgetObj3D = CoordinatesWidgetObj3D()
        self.coordinatesWidgetObj3D.show()

    def rotateWindow(self):
        angleWin = int(self.rotateWinAng.displayText())
        Window.rotateWindow(angleWin)

    def moveUp(self):
        Window.move([0, 15])

    def moveDown(self):
        Window.move([0, -15])

    def moveLeft(self):
        Window.move([-15, 0])

    def moveRight(self):
        Window.move([15, 0])

    def moveLookUp(self):
        Window.move([0, 15]) #alterar para ser o look

    def moveLookDown(self):
        Window.move([0, -15])#alterar para ser o look

    def moveLookLeft(self):
        Window.move([-15, 0])#alterar para ser o look

    def moveLookRight(self):
        Window.move([15, 0])#alterar para ser o look

    def zoomIn(self):
        Window.zoom(0.9)

    def zoomOut(self):
        Window.zoom(1.1)

    def chosenTecnic(self, checkBox):
        if checkBox.text() == "Cohen-Sutherland":
            if checkBox.isChecked():
                Window.LINECLIPPING = "CohenSutherland"
        if checkBox.text() == "Liang-Barsky":
            if checkBox.isChecked():
                Window.LINECLIPPING = "LiangBarsky"

    def importObject(self):
        (document, filter) = QFileDialog.getOpenFileName(self, 'Open file', './object', "(*.obj)")
        nameObject = document.split('/')[-1].replace('.obj', '')
        if document == "":
            return
        with open(document) as file:
            data = file.read()
            file_lines = [line.split(" ") for line in data.split("\n")]
            vertices = {}
            faces = []
            for number, line in enumerate(file_lines):
                if line[0] == "v":
                    vertices[number + 1] = [float(line[1]), float(line[2])]
                if line[0] == "f":
                    face = []
                    for index in line[1:]:
                        face.append(vertices[int(index)])
                    faces.append(face)
            for face in faces:
                World.addObject(Object2D(face, nameObject))

    def exportObject(self):
        if World.selectedObject is not None:
            (document, filter) = QFileDialog.getSaveFileName(self, 'Save File', './object', "(*.obj)")
            if document == "":
                return
            file = open(document, 'w')
            points = World.selectedObject.points
            text = ''
            faces = 'f'
            for (position, point) in enumerate(points):
                text += 'v ' + str(point.x) + ' ' + str(point.y) + ' 0\n'
                faces += ' ' + str(position + 1)
            text += faces + '\n'
            file.write(text)
            file.close()
