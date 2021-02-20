import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel
from object.objects import Objects
from object.point import Point


class TransformationWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Transformações 2D")
        self.setGeometry(300, 300, 400, 300)
        layout = QVBoxLayout()

        self.Confirma = QPushButton('rotate')
        self.Confirma.setStyleSheet('font-size: 30px')
        self.Confirma.setGeometry(0, 0, 200, 200)
        self.Confirma.clicked.connect(self.rotate)

        layout.addWidget(self.Confirma)
        self.setLayout(layout)

    def rotate(self):
        if (Objects.selectedObject is not None):
            centerPoint = Objects.selectedObject.getCenter()
            Objects.selectedObject.rotate(centerPoint, 45)