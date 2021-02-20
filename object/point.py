from object.object2D import Object2D
from PyQt5.QtCore import QPoint


class Point(QPoint, Object2D):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.label = "Point ({},{})".format(x, y)

    def draw(self, painter):
        pointsTransformed = self.transformViewport([self])[0]
        painter.drawPoint(pointsTransformed[0], pointsTransformed[1])
