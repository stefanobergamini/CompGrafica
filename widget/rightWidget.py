from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter
from object.objects import Objects


class RightWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 0, 800, 500)
        palette = self.palette()
        self.setAutoFillBackground(True)
        self.setPalette(palette)
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        for object in Objects.listObjects:
            object.draw(painter)
