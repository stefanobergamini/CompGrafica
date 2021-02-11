from PyQt5.QtWidgets import QGridLayout, QWidget

from widget.leftWidget import LeftWidget
from widget.rightWidget import RightWidget
from widget.objectsList import ObjectsList


class MainWidget(QWidget):

    def __init__(self):
        super().__init__()
        leftWidget = LeftWidget()
        leftWidget.show()

        rightWidget = RightWidget()
        rightWidget.show()

        objectsList = ObjectsList()
        objectsList.show()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(leftWidget, 1, 1, 1, 1)
        grid.addWidget(objectsList, 2, 1, 1, 1)
        grid.addWidget(rightWidget, 1, 2, 1, 4)
        self.setLayout(grid)
