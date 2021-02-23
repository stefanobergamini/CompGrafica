from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QGridLayout, QLineEdit, QLabel
from object.objects import Objects
from object.point import Point


class TransformationWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Transformações 2D")
        self.setGeometry(1225, 300, 400, 300)
        layout = QGridLayout()

        self.coordenadaX = QLineEdit()
        self.labelCoordX = QLabel('Coordinate of Anchor X:')

        self.coordenadaY = QLineEdit()
        self.labelCoordY = QLabel('Coordinate of Anchor Y:')

        self.angle = QLineEdit()
        self.angleLabel = QLabel('Angle of Rotation:')

        self.RotateWithPoint = QPushButton('Rotate around point')
        self.RotateWithPoint.setStyleSheet('font-size: 18px')
        self.RotateWithPoint.clicked.connect(self.rotateAroundPoint)

        self.RotateCenter = QPushButton('Rotate around center')
        self.RotateCenter.setStyleSheet('font-size: 18px')
        self.RotateCenter.clicked.connect(self.rotateAroundCenter)

        self.RotateOrigin = QPushButton('Rotate around origin')
        self.RotateOrigin.setStyleSheet('font-size: 18px')
        self.RotateOrigin.clicked.connect(self.rotateAroundOrigin)

        self.ClearLabels = QPushButton('Clear Rotation Labels')
        self.ClearLabels.setStyleSheet('font-size: 18px')
        self.ClearLabels.clicked.connect(self.clearLabelsRotation)

        # END OF THE ROTATION PART START OF THE TRANSLATION ----------------

        self.pointX = QLineEdit()
        self.labelPointX = QLabel('Point X:')

        self.pointY = QLineEdit()
        self.labelPointY = QLabel('Point Y:')

        self.Translation = QPushButton('Translate to Point')
        self.Translation.setStyleSheet('font-size: 18px')
        self.Translation.clicked.connect(self.translationAroundPoint)

        self.ClearLabelsTranslation = QPushButton('Clear Translation Labels')
        self.ClearLabelsTranslation.setStyleSheet('font-size: 18px')
        self.ClearLabelsTranslation.clicked.connect(self.clearLabelsTranslation)

        # END OF THE TRANSLATION PART START OF THE SCALE -------------------

        self.scaleX = QLineEdit()
        self.labelScaleX = QLabel('Scale X:')

        self.scaleY = QLineEdit()
        self.labelScaleY = QLabel('Scale Y:')

        self.Scale = QPushButton('Scale to the amount designated')
        self.Scale.setStyleSheet('font-size: 18px')
        self.Scale.clicked.connect(self.scaling)

        self.ClearLablesScale = QPushButton('Clear Scale Lables')
        self.ClearLablesScale.setStyleSheet('font-size: 18px')
        self.ClearLablesScale.clicked.connect(self.clearLabelsScale)

        # END OF CREATIONS OF WIDGETS START OF LAYOUT ADDING

        layout.addWidget(self.labelCoordX, 0, 0)
        layout.addWidget(self.coordenadaX, 1, 0)
        layout.addWidget(self.labelCoordY, 2, 0)
        layout.addWidget(self.coordenadaY, 3, 0)
        layout.addWidget(self.angleLabel, 4, 0)
        layout.addWidget(self.angle, 5, 0)
        layout.addWidget(self.RotateWithPoint, 6, 0)
        layout.addWidget(self.RotateCenter, 7, 0)
        layout.addWidget(self.RotateOrigin, 8, 0)
        layout.addWidget(self.ClearLabels, 9, 0)

        # END OF ADDWIDGET FOR ROTATION START OF TRANSLATION

        layout.addWidget(self.labelPointX, 0, 1)
        layout.addWidget(self.pointX, 1, 1)
        layout.addWidget(self.labelPointY, 2, 1)
        layout.addWidget(self.pointY, 3, 1)
        layout.addWidget(self.Translation, 4, 1)
        layout.addWidget(self.ClearLabelsTranslation, 5, 1)


        # END OF ADDWIDGET FOR TRANSLATION START OF SCALE

        layout.addWidget(self.labelScaleX, 0, 2)
        layout.addWidget(self.scaleX, 1, 2)
        layout.addWidget(self.labelScaleY, 2, 2)
        layout.addWidget(self.scaleY, 3, 2)
        layout.addWidget(self.Scale, 4, 2)
        layout.addWidget(self.ClearLablesScale, 5, 2)
        self.setLayout(layout)

    def rotateAroundPoint(self):
        if (Objects.selectedObject is not None):
            if (self.coordenadaX.displayText() == "" or self.coordenadaY.displayText() == "" or self.angle.displayText() == ""):
                return
            x = int(self.coordenadaX.displayText())
            y = int(self.coordenadaY.displayText())
            receivedAngle = int(self.angle.displayText())
            anchorPoint = Point(x, y)
            Objects.selectedObject.rotate(anchorPoint, receivedAngle)

    def rotateAroundCenter(self):
        if (Objects.selectedObject is not None):
            if (self.coordenadaX.displayText() == "" or self.coordenadaY.displayText() == "" or self.angle.displayText() == ""):
                return
            receivedAngle = int(self.angle.displayText())
            center = Objects.selectedObject.getCenter()
            Objects.selectedObject.rotate(center, receivedAngle)

    def rotateAroundOrigin(self):
        if (Objects.selectedObject is not None):
            if (self.coordenadaX.displayText() == "" or self.coordenadaY.displayText() == "" or self.angle.displayText() == ""):
                return
            receivedAngle = int(self.angle.displayText())
            origin = Point(0, 0)
            Objects.selectedObject.rotate(origin, receivedAngle)

    def translationAroundPoint(self):
        if (Objects.selectedObject is not None):
            if (self.pointX.displayText() == "" or self.pointY.displayText() == ""):
                return
            x = int(self.pointX.displayText())
            y = int(self.pointY.displayText())
            point = Point(x, y)
            Objects.selectedObject.translation(point)

    def scaling(self):
        if (Objects.selectedObject is not None):
            if (self.scaleX.displayText() == "" or self.scaleY.displayText() == ""):
                return
            x = int(self.scaleX.displayText())
            y = int(self.scaleY.displayText())
            Objects.selectedObject.scale(x, y)

    def clearLabelsRotation(self):
        self.coordenadaX.clear()
        self.coordenadaY.clear()
        self.angle.clear()

    def clearLabelsTranslation(self):
        self.pointX.clear()
        self.pointY.clear()
        self.angle.clear()

    def clearLabelsScale(self):
        self.scaleX.clear()
        self.scaleY.clear()
        self.angle.clear()