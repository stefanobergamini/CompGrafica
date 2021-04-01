from PyQt5.QtCore import QRectF, QPoint
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPalette, QColor
from PyQt5 import QtCore
from models.viewport import Viewport
from models.window import Window
from operations.clipping import Clipping

[xmin, ymin], [xmax, ymax] = Window.expanded_boundaries()
xini = ((0 - xmin) / (xmax - xmin)) * (Viewport.xmax - Viewport.xmin)
yini = (1 - ((0 - ymin) / (ymax - ymin))) * (Viewport.ymax - Viewport.ymin)
xfin = ((800 - xmin) / (xmax - xmin)) * (Viewport.xmax - Viewport.xmin)
yfin = (1 - ((450 - ymin) / (ymax - ymin))) * (Viewport.ymax - Viewport.ymin)
rect = QRectF(QPoint(xini, yini), QPoint(xfin, yfin))


class RightWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(Viewport.xmax, Viewport.ymax)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor('white'))
        self.setPalette(palette)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000/60)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawRoundedRect(rect, 1, 1)
        Window.normalizedObjects()
        Clipping().clip(Window.listObjects)
        Viewport.transformViewport()
        for object in Viewport.listObjects:
            object.draw(painter)
