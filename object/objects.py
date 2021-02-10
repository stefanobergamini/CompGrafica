from object.point import Point
from object.line import Line
from object.polygon import Polygon
from PyQt5.QtCore import QPoint


class Objects:
    listObjects = [Polygon([Point(10,10), Point(10,100), Point(100,10), Point(100,100)])]

    @staticmethod
    def clearObjects(object):
        Objects.listObjects = []

    @staticmethod
    def addObject(object):
        Objects.listObjects.append(object)
