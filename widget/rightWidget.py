from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QWidget
from PyQt5.QtGui import QColor, QPalette

class RightWidget(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 0, 800, 500)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor('red'))
        self.setPalette(palette)
