import sys

from PyQt5.QtWidgets import QListWidget, QWidget, QVBoxLayout, QLabel
from object.objects import Objects


class ObjectsList(QWidget):

    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout(self)
        listWidget = QListWidget()

        listWidget.addItem("1")
        listWidget.addItem("1")

        vbox.addWidget(QLabel('Objetos:'))
        vbox.addWidget(listWidget)


