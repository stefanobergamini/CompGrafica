from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QPoint
from object.object2D import Object2D


class Point(QPoint, Object2D):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.label = "Point [{}, {}] coordenates".format(x, y)

    def draw(self, painter):
        pointsTransformed = self.transformViewport([self])[0]
        pointTransformed = Point(pointsTransformed[0], pointsTransformed[1])
        painter.drawPoint(pointTransformed)
