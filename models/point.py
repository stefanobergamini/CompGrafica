from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter

class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getCoordinates(self):
        return { self.x, self.y }

    def paintEvent(self, event):
        
        painter = QPainter()

        painter.begin(self)

        painter.setRenderHint(QPainter.Antialiasing)

        painter.setPen(Qt.red)

        painter.setBrush(Qt.white)

        painter.drawLine(400, 100, 100, 100)

