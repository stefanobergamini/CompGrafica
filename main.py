import sys
from PyQt5.QtWidgets import QApplication
from windows.mainWindow import MainWindow
from PyQt5 import QtCore


class Main():
    def __init__(self):
        app = QApplication(sys.argv)

        mainWindow = MainWindow()
        mainWindow.show()

        sys.exit(app.exec_())
        app.exec_()


Main()
