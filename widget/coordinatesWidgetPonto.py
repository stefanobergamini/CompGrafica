import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel
from PyQt5.QtGui import QColor
from models.world import World
from models.point import Point
from models.object import Object


class CoordinatesWidgetPonto(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ponto")
        self.setGeometry(300, 300, 200, 100)
        layout = QVBoxLayout()

        self.coordenadaX = QLineEdit()
        self.coordenadaY = QLineEdit()
        self.colorPoint = QLineEdit()

        layout.addWidget(QLabel('Coordenada X:'))
        layout.addWidget(self.coordenadaX)
        layout.addWidget(QLabel('Coordenada Y:'))
        layout.addWidget(self.coordenadaY)
        layout.addWidget(QLabel('Color: r,g,b (between 0 and 255)'))
        layout.addWidget(self.colorPoint)

        self.Confirma = QPushButton('Confirmar')
        self.Confirma.setStyleSheet('font-size: 30px')
        layout.addWidget(self.Confirma)
        self.Confirma.clicked.connect(self.printXeY)

        self.Limpar = QPushButton('Limpar')
        self.Limpar.setStyleSheet('font-size: 15px')
        layout.addWidget(self.Limpar)
        self.Limpar.clicked.connect(self.clearLabels)
        self.setLayout(layout)

    def printXeY(self):
        if (self.coordenadaX.displayText() == "" or self.coordenadaY.displayText() == ""):
            return
        x = int(self.coordenadaX.displayText())
        y = int(self.coordenadaY.displayText())
        if (self.colorPoint.displayText() == ""):
            r, g, b = 0, 0, 0
            color = QColor(int(r), int(g), int(b))
        else:
            r, g, b = self.colorPoint.displayText().strip().split(',')
            color = QColor(int(r), int(g), int(b))
        point = Point(x, y)
        newObject = Object([point], 'Point', color)
        World.addObject(newObject)
        self.close()
        self.clearLabels()

    def clearLabels(self):
        self.coordenadaX.clear()
        self.coordenadaY.clear()
