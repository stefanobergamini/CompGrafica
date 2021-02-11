from PyQt5.QtGui import QPolygon
from object.object2D import Object2D
from object.point import Point


class Wireframe(QPolygon, Object2D):
    def __init__(self, points):
        super().__init__(points)
        self.points = points
        self.label = "Wireframe {} points".format(points)

    def draw(self, painter):
        cordinatesTransformed = self.transformViewport(self.points)
        points = []
        for cordinateTransformed in cordinatesTransformed:
            points.append(Point(cordinateTransformed[0], cordinateTransformed[1]))
        polygonTransformed = Wireframe(points)
        painter.drawPolygon(polygonTransformed)
