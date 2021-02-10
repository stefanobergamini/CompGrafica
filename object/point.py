from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QPoint


class Point(QPoint):
    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, painter):
        painter.drawPoint(self)