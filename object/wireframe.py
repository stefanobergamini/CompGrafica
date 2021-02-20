from object.object2D import Object2D
from object.point import Point
from object.objects import Objects


class Wireframe(Object2D):
    def __init__(self, points):
        self.points = points
        self.label = "#{}: Wireframe Points: {}".format(Objects.numberObjects,
            self.formatPointsLabel(points))

    def formatPointsLabel(self, points):
        pointsLabel = ""
        for point in points:
            pointsLabel += "({},{}) ".format(point.x, point.y)
        return pointsLabel

    def draw(self, painter):
        cordinatesTransformed = self.transformViewport(self.points)
        transformedPoints = []
        for cordinateTransformed in cordinatesTransformed:
            transformedPoints.append(Point(cordinateTransformed[0], cordinateTransformed[1]))

        if (len(transformedPoints) == 1):
            painter.drawPoint(transformedPoints[0])
        elif (len(transformedPoints) == 2):
            painter.drawLine(transformedPoints[0], transformedPoints[1])
        else:
            for position in range(0, len(transformedPoints)):
                if(position < (len(transformedPoints) - 1)):
                    painter.drawLine(
                        transformedPoints[position], transformedPoints[position+1])
                else:
                    painter.drawLine(
                        transformedPoints[position], transformedPoints[0])

    def rotate(self, anchorPoint, angle):
        coordinates = self.rotateObject(self.points, anchorPoint, angle)
        wireframeRotate = []
        for coordinate in coordinates:
            x, y, _ = coordinate
            wireframeRotate.append(Point(x, y))
        self.points = wireframeRotate

    def translation(self, anchorPoint):
        coordinates = self.translationObject(self.points, anchorPoint)
        wireframeTranslation = []
        for coordinate in coordinates:
            x, y, _ = coordinate
            wireframeTranslation.append(Point(x, y))
        self.points = wireframeTranslation

    def scale(self, scaleX, scaleY):
        coordinates = self.scaleObject(self.points, scaleX, scaleY)
        wireframeScale = []
        for coordinate in coordinates:
            x, y, _ = coordinate
            wireframeScale.append(Point(x, y))
        self.points = wireframeScale

    def getCenter(self):
        cx, cy = self.getCenterObject(self.points)
        return Point(cx, cy)
