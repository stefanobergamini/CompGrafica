import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel, QCheckBox
from PyQt5.QtGui import QColor
from models.world import World
from models.point import Point
from models.object import Object
from models.curve import Curve
from models.spline import Spline


class CoordinatesWidgetCurve(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Curve")
        self.setGeometry(300, 300, 200, 100)
        self.layout = QVBoxLayout()

        self.coordenadaXY = QLineEdit()
        self.colorCurve = QLineEdit()

        self.layout.addWidget(QLabel('Todas as coordenada X e Y: x1,y1;x2,y2;x3,y3;x4,y4'))
        self.layout.addWidget(self.coordenadaXY)
        self.layout.addWidget(QLabel('Color: r,g,b (between 0 and 255)'))
        self.layout.addWidget(self.colorCurve)

        self.Confirma = QPushButton('Confirmar')
        self.Confirma.setStyleSheet('font-size: 30px')
        self.layout.addWidget(self.Confirma)
        self.Confirma.clicked.connect(self.printXeY)
        self.setLayout(self.layout)

        self.limpar = QPushButton('Limpar')
        self.limpar.setStyleSheet('font-size: 15px')
        self.layout.addWidget(self.limpar)
        self.limpar.clicked.connect(self.clearLabels)
        self.setLayout(self.layout)

    def printXeY(self):
        newpontos = []
        coordenadasXY = self.coordenadaXY.displayText().strip().split(';')
        for stringPonto in coordenadasXY:
            if(stringPonto != ''):
                x, y = stringPonto.split(',')
                newpontos.append(Point(int(x), int(y)))
        if (self.colorCurve.displayText() == ""):
            r, g, b = 0, 0, 0
            color = QColor(int(r), int(g), int(b))
        else:
            r, g, b = self.colorCurve.displayText().strip().split(',')
            color = QColor(int(r), int(g), int(b))
        World.addObject(Spline(newpontos, color))
        self.close()
        self.clearLabels()

    def clearLabels(self):
        self.coordenadaXY.clear()
        self.colorCurve.clear()
