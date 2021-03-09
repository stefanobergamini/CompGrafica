import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel
from models.world import World
from models.point import Point
from models.object import Object
from widget.objectsList import ObjectsList


class CoordinatesWidgetLinha(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Linha")
        self.setGeometry(300, 300, 200, 100)
        layout = QVBoxLayout()

        self.coordenadaX1 = QLineEdit()
        self.coordenadaY1 = QLineEdit()
        self.coordenadaX2 = QLineEdit()
        self.coordenadaY2 = QLineEdit()
        self.colorLine = QLineEdit()

        layout.addWidget(QLabel('Coordenada X1:'))
        layout.addWidget(self.coordenadaX1)
        layout.addWidget(QLabel('Coordenada Y1:'))
        layout.addWidget(self.coordenadaY1)
        layout.addWidget(QLabel('Coordenada X2:'))
        layout.addWidget(self.coordenadaX2)
        layout.addWidget(QLabel('Coordenada Y2:'))
        layout.addWidget(self.coordenadaY2)
        layout.addWidget(QLabel('Color:'))
        layout.addWidget(self.colorLine)

        self.Confirma = QPushButton('Confirmar')
        self.Confirma.setStyleSheet('font-size: 30px')
        layout.addWidget(self.Confirma)
        self.Confirma.clicked.connect(self.printXeY)
        self.setLayout(layout)

        self.limpar = QPushButton('Limpar')
        self.limpar.setStyleSheet('font-size: 15px')
        layout.addWidget(self.limpar)
        self.limpar.clicked.connect(self.clearLabels)
        self.setLayout(layout)

    def printXeY(self):
        if (self.coordenadaX1.displayText() == "" or self.coordenadaY1.displayText() == "" or
                self.coordenadaX2.displayText() == "" or self.coordenadaY2.displayText() == ""):
            return
        color = int (self.colorLine.displayText())
        x1 = int(self.coordenadaX1.displayText())
        y1 = int(self.coordenadaY1.displayText())
        ponto1 = Point(x1, y1)
        x2 = int(self.coordenadaX2.displayText())
        y2 = int(self.coordenadaY2.displayText())
        ponto2 = Point(x2, y2)

        line = Object([ponto1, ponto2], "Line")
        World.addObject(line)
        self.close()
        self.clearLabels()

    def clearLabels(self):
        self.coordenadaX1.clear()
        self.coordenadaY1.clear()
        self.coordenadaX2.clear()
        self.coordenadaY2.clear()
