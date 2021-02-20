from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPalette, QColor
from PyQt5 import QtCore
from object.objects import Objects
from windows.viewport import Viewport


class RightWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 0, Viewport.xmax, Viewport.ymax)
        self.setFixedSize(Viewport.xmax, Viewport.ymax)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor('white'))
        self.setPalette(palette)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(5000)

    def paintEvent(self, event):
        painter = QPainter(self)
        for object in Objects.listObjects:
            object.draw(painter)
