from PyQt5.QtGui import QBrush, QPainterPath
from models.object2D import Object2D
from models.point import Point
from models.world import World
from PyQt5.QtCore import Qt

class Object(Object2D):
    def __init__(self, points, type, color, filled):
        self.points = points
        self.color = color
        self.filled = filled
        self.type = type
        self.label = "#{}: {}".format(World.numberObjects, self.type)

    def setType(self, type):
        self.type = type

    def setPoints(self, points):
        self.points = points

    def draw(self, painter):
        path = QPainterPath()
        painter.setPen(self.color)
        if (len(self.points) == 1):
            painter.drawPoint(self.points[0])
        elif (len(self.points) == 2):
            painter.drawLine(self.points[0], self.points[1])
        else:
            path.moveTo(self.points[0])
            for position in range(0, len(self.points)):
                if(position < (len(self.points))):
                    path.lineTo(self.points[position])
                else:
                    path.lineTo(self.points[0])
            if self.filled == True:
                painter.setBrush(QBrush(self.color, Qt.SolidPattern))
            painter.drawPath(path)

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

    def normalized(self, centerPoint, angle, factor):
        coordinates = self.normalizedObjects(self.points, centerPoint, angle, factor)
        wireframeCoordinates = []
        for coordinate in coordinates:
            x, y, _ = coordinate
            wireframeCoordinates.append(Point(x, y))
        self.points = wireframeCoordinates
