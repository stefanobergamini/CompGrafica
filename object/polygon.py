from PyQt5.QtGui import QPolygon
from object.point import Point
from windows.viewport import Viewport
from windows.window import Window

class Polygon(QPolygon):
    def __init__(self, points):
        super().__init__(points)
        self.points = points

    def draw(self, painter):
        polygonTranformed = self.transformViewport()
        painter.drawPolygon(polygonTranformed)

    def transformViewport(self):
        listOfPoints = []
        for point in self.points:
            xvp = ((point.x() - Window.xmin) / (Window.xmax - Window.xmin)) * (Viewport.xmax - Viewport.xmin)
            yvp = (1- ( (point.y() - Window.ymin) / (Window.ymax - Window.ymin) ) ) * (Viewport.ymax - Viewport.ymin)
            listOfPoints.append(Point(xvp, yvp))
        return Polygon(listOfPoints)