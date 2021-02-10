from PyQt5.QtGui import QPolygon, QVector2D


class Polygon(QPolygon):
    def __init__(self, points):
        super().__init__(points)

    def draw(self, painter):
        painter.drawPolygon(self)
