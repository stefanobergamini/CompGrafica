from PyQt5.QtGui import QPainter


class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, painter):
        painter.drawLine(self.point1, self.point2)
