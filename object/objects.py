from object.point import Point
from object.line import Line
from object.polygon import Polygon
from PyQt5.QtCore import QPoint


class Objects:
    listObjects = []

    @staticmethod
    def clearObjects(object):
        Objects.listObjects = []

    @staticmethod
    def addObject(object):
        Objects.listObjects.append(object)
