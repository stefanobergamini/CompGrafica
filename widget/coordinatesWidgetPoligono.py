import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel


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
        print(self.coordenadaXY.displayText())

    def clearLabels(self):
        self.coordenadaXY.clear()