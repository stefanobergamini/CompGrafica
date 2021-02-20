from object.object2D import Object2D
from PyQt5.QtCore import QPoint
from object.objects import Objects


class Point(QPoint, Object2D):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.label = "#{}: Point ({},{})".format(Objects.numberObjects, x, y)

    def draw(self, painter):
        pointsTransformed = self.transformViewport([self])[0]
        painter.drawPoint(pointsTransformed[0], pointsTransformed[1])

    def rotate(self, anchorPoint, angle):
        coordinates = self.rotateObject([self], anchorPoint, angle)[0]
        x, y, _ = coordinates
        self.x = x
        self.y = y

    def translation(self, anchorPoint):
        coordinates = self.translationObject([self], anchorPoint)[0]
        x, y, _ = coordinates
        self.x = x
        self.y = y

    def scale(self, scaleX, scaleY):
        coordinates = self.scaleObject([self], scaleX, scaleY)[0]
        x, y, _ = coordinates
        self.x = x
        self.y = y

    def getCenter(self):
        return self
