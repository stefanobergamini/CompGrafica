import numpy
from windows.viewport import Viewport
from windows.window import Window


class Object2D:
    def transformViewport(self, points):
        listOfPoints = []
        for point in points:
            xvp = ((point.x - Window.xmin) / (Window.xmax - Window.xmin)) * (Viewport.xmax - Viewport.xmin)
            yvp = (1 - ( (point.y - Window.ymin) / (Window.ymax - Window.ymin) ) ) * (Viewport.ymax - Viewport.ymin)
            listOfPoints.append([xvp, yvp])
        return listOfPoints

    def rotateObject(self, points, anchorPoint):
        objectRotate = []
        rotateAngle = self.getAngleInRadianus(Window.angle)
        for point in points:
            pointMatrix = [point.x, point.y, 1]
            translateMatrixToCenter = [[1, 0, 0], [0, 1, 0], [-anchorPoint.x, -anchorPoint.y, 1]]
            rotatePoint = numpy.dot(pointMatrix, translateMatrixToCenter)
            rotateMatrix = [[numpy.cos(rotateAngle), -numpy.sin(rotateAngle), 0], [numpy.sin(rotateAngle), numpy.cos(rotateAngle), 0], [0, 0, 1]]
            rotatePoint = numpy.dot(rotatePoint, rotateMatrix)
            translateMatrixBack = [[1, 0, 0], [0, 1, 0], [anchorPoint.x, anchorPoint.y, 1]]
            rotatePoint = numpy.dot(rotatePoint, translateMatrixBack)
            objectRotate.append(rotatePoint)
        return objectRotate

    def getAngleInRadianus(self, angle):
        return angle * numpy.pi/180
