import sys

from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QWidget, QVBoxLayout, QLabel
from PyQt5 import QtCore
from object.objects import Objects


class ObjectsList(QWidget):

    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout(self)
        self.listWidget = QListWidget()
        self.objectListRendered = []

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.renderObjectList)
        self.timer.start(1000)

        vbox.addWidget(QLabel('Objects:'))
        vbox.addWidget(self.listWidget)

    def renderObjectList(self):
        if(Objects.listObjects == self.objectListRendered):
            return
        self.listWidget.clear()
        for object in Objects.listObjects:
            listWidgetItem = QListWidgetItem(object.label)
            self.listWidget.addItem(listWidgetItem)
        self.objectListRendered = Objects.listObjects.copy()

