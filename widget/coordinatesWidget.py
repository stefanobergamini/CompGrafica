import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel


class CoordinatesWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 100, 100)
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
        self.setLayout(layout)

    def printXeY(self):
        print(self.coordenadaX.displayText())
        print(self.coordenadaY.displayText())
