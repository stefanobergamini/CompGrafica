import numpy
from models.world import World
from models.point import Point
from models.object import Object


class Window():
    xmin = 0
    xmax = 800
    ymin = 0
    ymax = 450
    listObjects = []
    angle = 0

    @staticmethod
    def SCN():
        wcx, wcy = Window.getCenterWindow()
        windowAngle = Window.getWindowAngleInRadianus()
        scn = []
        translateWindowToCenter = [[1, 0, 0], [0, 1, 0], [-wcx, -wcy, 1]]
        rotateWindow = [[numpy.cos(windowAngle), -numpy.sin(windowAngle), 0], [numpy.sin(windowAngle), numpy.cos(windowAngle), 0], [0, 0, 1]]
        scaleWindow = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        scn = numpy.dot(translateWindowToCenter, rotateWindow)
        scn = numpy.dot(scn, scaleWindow)
        return scn

    @staticmethod
    def transformSCN():
        Window.listObjects = []
        for object in World.listObjects:
            Object(object.points, object.type)
            Window.listObjects.append(Object(object.points, object.type))
        print(Window.listObjects)

    @staticmethod
    def rotateWindow(angle):
        Window.angle += angle


    @staticmethod
    def getCenterWindow():
        wcx = (Window.xmin + Window.xmax) / 2
        wcy = (Window.ymin + Window.ymax) / 2
        return [wcx, wcy]

    @staticmethod
    def getWindowAngleInRadianus():
        return Window.angle * numpy.pi/180

    @staticmethod
    def moveLeft():
        Window.xmin -= 5
        Window.xmax -= 5

    @staticmethod
    def moveRight():
        Window.xmin += 5
        Window.xmax += 5

    @staticmethod
    def moveDown():
        Window.ymin -= 5
        Window.ymax -= 5

    @staticmethod
    def moveUp():
        Window.ymin += 5
        Window.ymax += 5

    @staticmethod
    def zoomIn():
        if ((Window.ymax > (Window.ymin + 50)) and (Window.xmax > (Window.xmin + 50))):
            Window.ymin += 5
            Window.ymax -= 5
            Window.xmin += 5
            Window.xmax -= 5

    @staticmethod
    def zoomOut():
        Window.ymin -= 5
        Window.ymax += 5
        Window.xmin -= 5
        Window.xmax += 5
