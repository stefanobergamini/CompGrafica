import numpy
from models.world import World
from models.window import Window
from models.point import Point
from models.object import Object


class Viewport():
    xmin = 0
    xmax = 800
    ymin = 0
    ymax = 450
    listObjects = []

    @staticmethod
    def transformViewport():
        Viewport.listObjects = []

        (xmin, ymin), (xmax, ymax) = Window.expanded_boundaries()
        for object in Window.listObjects:
            listPoints = []
            for point in object.points:
                xvp = ((point.x - xmin) / (xmax - xmin)) * (Viewport.xmax - Viewport.xmin)
                yvp = (1 - ((point.y - ymin) / (ymax - ymin))) * (Viewport.ymax - Viewport.ymin)
                listPoints.append(Point(xvp, yvp))
            Viewport.listObjects.append(Object(listPoints, object.type))