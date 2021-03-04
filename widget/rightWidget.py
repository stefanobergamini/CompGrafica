from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPalette, QColor
from PyQt5 import QtCore
from models.viewport import Viewport
from models.window import Window
from models.point import Point


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
        painter.drawRoundedRect(5, 5, Viewport.xmax, Viewport.ymax, 3, 3);

        Viewport.transformViewport()
        for object in Viewport.listObjects:
            object.draw(painter)
