from object.object2D import Object2D
from object.point import Point
from object.objects import Objects


class Line(Object2D):
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.label = "#{}: Line Points: {}".format(Objects.numberObjects,
            self.formatPointsLabel([point1, point2]))

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

    def rotate(self, anchorPoint, angle):
        coordinates1, coordinates2 = self.rotateObject([self.point1, self.point2], anchorPoint, angle)
        self.point1 = Point(coordinates1[0], coordinates1[1])
        self.point2 = Point(coordinates2[0], coordinates2[1])

    def getCenter(self):
        cx, cy = self.getCenterObject([self.point1, self.point2])
        return Point(cx, cy)
