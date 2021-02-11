import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel
from object.objects import Objects
from object.point import Point
from widget.objectsList import ObjectsList

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
        x = int(self.coordenadaX.displayText())
        y = int(self.coordenadaY.displayText())
        point = Point(x, y)
        Objects.addObject(point)
        self.close()
        self.clearLabels()

    def clearLabels(self):
        self.coordenadaX.clear()
        self.coordenadaY.clear()
