from PyQt5.QtGui import QPainter
from object.object2D import Object2D
from object.point import Point


class Line(Object2D):
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, painter):
        cordinatesTransformed = self.transformViewport([self.point1, self.point2])
        listpoints = []
        for cordinateTransformed in cordinatesTransformed:
            listpoints.append(Point(cordinateTransformed[0], cordinateTransformed[1]))
        painter.drawLine(listpoints[0], listpoints[1])
