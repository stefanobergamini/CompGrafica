from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QPoint
from windows.viewport import Viewport
from windows.window import Window


class Point(QPoint):
    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, painter):
        pointerTransformed = self.transformViewport()
        painter.drawPoint(pointerTransformed)

    def transformViewport(self):
        xvp = ((self.x() - Window.xmin) / (Window.xmax - Window.xmin)) * (Viewport.xmax - Viewport.xmin)
        yvp = (1- ( (self.y() - Window.ymin) / (Window.ymax - Window.ymin) ) ) * (Viewport.ymax - Viewport.ymin)
        return Point(xvp, yvp)