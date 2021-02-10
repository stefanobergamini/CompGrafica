from PyQt5.QtGui import QPainter
from object.point import Point
from windows.viewport import Viewport
from windows.window import Window

class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, painter):
        lineTransformed = self.transformViewport()
        painter.drawLine(lineTransformed[0], lineTransformed[1])

    def transformViewport(self):
        xvp1 = ((self.point1.x() - Window.xmin) / (Window.xmax - Window.xmin)) * (Viewport.xmax - Viewport.xmin)
        yvp1 = (1- ( (self.point1.y() - Window.ymin) / (Window.ymax - Window.ymin) ) ) * (Viewport.ymax - Viewport.ymin)
        point1 = Point(xvp1, yvp1)
        xvp2 = ((self.point2.x() - Window.xmin) / (Window.xmax - Window.xmin)) * (Viewport.xmax - Viewport.xmin)
        yvp2 = (1- ( (self.point2.y() - Window.ymin) / (Window.ymax - Window.ymin) ) ) * (Viewport.ymax - Viewport.ymin)
        point2 = Point(xvp2, yvp2)
        return (point1, point2)