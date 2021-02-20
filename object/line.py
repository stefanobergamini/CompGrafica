from object.object2D import Object2D
from object.point import Point


class Line(Object2D):
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.label = "Line Points: {}".format(
            self.formatPointsLabel([point1, point2]))
        self.angle = 0

    def formatPointsLabel(self, points):
        pointsLabel = ""
        for point in points:
            pointsLabel += "({},{}) ".format(point.x, point.y)
        return pointsLabel

    def draw(self, painter):
        cordinatesTransformed = self.transformViewport([self.point1, self.point2])
        listpoints = []
        for cordinateTransformed in cordinatesTransformed:
            listpoints.append(Point(cordinateTransformed[0], cordinateTransformed[1]))
        painter.drawLine(listpoints[0], listpoints[1])
