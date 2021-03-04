from models.world import World
from models.window import Window
from models.point import Point
from models.object import Object


class Viewport():
    xmin = 0
    xmax = 790
    ymin = 0
    ymax = 440
    listObjects = []

    @staticmethod
    def transformViewport():
        Viewport.listObjects = []
        Window.listObjects = []

        wcx, wcy = Window.center()
        windowAngle = Window.angle()
        for object in World.listObjects:
            rotateObject = Object(object.points, object.type)
            rotateObject.rotate(Point(wcx, wcy), windowAngle)
            Window.listObjects.append(rotateObject)

        (xmin, ymin), (xmax, ymax) = Window.boundaries()
        print(Window.boundaries())
        for object in Window.listObjects:
            listPoints = []
            for point in object.points:
                xvp = ((point.x - xmin) / (xmax - xmin)) * (Viewport.xmax - Viewport.xmin) + 10
                yvp = (1 - ((point.y - ymin) / (ymax - ymin))) * (Viewport.ymax - Viewport.ymin) + 10
                listPoints.append(Point(xvp, yvp))
            Viewport.listObjects.append(Object(listPoints, object.type))