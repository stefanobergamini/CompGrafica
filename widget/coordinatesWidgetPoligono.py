import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel
from object.objects import Objects
from object.point import Point
from object.wireframe import Wireframe
from widget.objectsList import ObjectsList

class CoordinatesWidgetPoligono(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Linha")
        self.setGeometry(300, 300, 200, 100)
        self.layout = QVBoxLayout()

        self.coordenadaXY = QLineEdit()

        self.layout.addWidget(QLabel('Todas as coordenada X e Y: [x1,y1] [x2,y2]'))
        self.layout.addWidget(self.coordenadaXY)

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
        coordenadasXY = self.coordenadaXY.displayText().split(' ')
        for stringPonto in coordenadasXY:
            pontoArray = stringPonto.replace('[', '').replace(']', '').split(',')
            newpontos.append(Point(int(pontoArray[0]), int(pontoArray[1])))
<<<<<<< Updated upstream
        Objects.addObject(Wireframe(newpontos))
=======
        Objects.addObject(Polygon(newpontos))
        ObjectsList.addObject()
>>>>>>> Stashed changes
        self.close()
        self.clearLabels()

    def clearLabels(self):
        self.coordenadaXY.clear()