import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel, QCheckBox
from PyQt5.QtGui import QColor
from models.world import World
from models.point import Point
from models.object import Object
from models.curve import Curve


class CoordinatesWidgetPoligono(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wireframe")
        self.setGeometry(300, 300, 200, 100)
        self.layout = QVBoxLayout()

        self.coordenadaXY = QLineEdit()
        self.colorPoligono = QLineEdit()

        self.layout.addWidget(QLabel('Todas as coordenada X e Y: x1,y1;x2,y2'))
        self.layout.addWidget(self.coordenadaXY)
        self.layout.addWidget(QLabel('Color: r,g,b (between 0 and 255)'))
        self.layout.addWidget(self.colorPoligono)

        self.b1 = QCheckBox("Filled Poligon")
        self.b1.setChecked(False)
        self.layout.addWidget(self.b1)

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
        if (self.colorPoligono.displayText() == ""):
            r, g, b = 0, 0, 0
            color = QColor(int(r), int(g), int(b))
        else:
            r, g, b = self.colorPoligono.displayText().strip().split(',')
            color = QColor(int(r), int(g), int(b))
        if self.b1.isChecked() == True:
            filled = True
        else:
            filled = False
        World.addObject(Curve(newpontos, color))
        self.close()
        self.clearLabels()

    def clearLabels(self):
        self.coordenadaXY.clear()