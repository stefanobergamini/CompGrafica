import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel


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

        layout.addWidget(QLabel('Coordenada X1:'))
        layout.addWidget(self.coordenadaX1)
        layout.addWidget(QLabel('Coordenada Y1:'))
        layout.addWidget(self.coordenadaY1)
        layout.addWidget(QLabel('Coordenada X2:'))
        layout.addWidget(self.coordenadaX2)
        layout.addWidget(QLabel('Coordenada Y2:'))
        layout.addWidget(self.coordenadaY2)

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
        print(self.coordenadaX1.displayText())
        print(self.coordenadaY1.displayText())
        print(self.coordenadaX2.displayText())
        print(self.coordenadaY2.displayText())

    def clearLabels(self):
        self.coordenadaX1.clear()
        self.coordenadaY1.clear()
        self.coordenadaX2.clear()
        self.coordenadaY2.clear()
