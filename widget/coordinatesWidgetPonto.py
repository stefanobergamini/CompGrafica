import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel
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

        layout.addWidget(QLabel('Coordenada X:'))
        layout.addWidget(self.coordenadaX)
        layout.addWidget(QLabel('Coordenada Y:'))
        layout.addWidget(self.coordenadaY)

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
        point = Point(x, y)
        newObject = Object([point], 'Point')
        World.addObject(newObject)
        self.close()
        self.clearLabels()

    def clearLabels(self):
        self.coordenadaX.clear()
        self.coordenadaY.clear()
