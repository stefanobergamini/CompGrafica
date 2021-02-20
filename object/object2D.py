import numpy
from windows.viewport import Viewport
from windows.window import Window


class Object2D:
    def transformViewport(self, points):
        listOfPoints = []
        for point in points:
            xvp = ((point.x - Window.xmin) / (Window.xmax - Window.xmin)) * (Viewport.xmax - Viewport.xmin)
            yvp = (1- ( (point.y - Window.ymin) / (Window.ymax - Window.ymin) ) ) * (Viewport.ymax - Viewport.ymin)
            listOfPoints.append([xvp, yvp])
        return listOfPoints

    def rotatePoint(self, point, anchorPoint):
        pointMatrix = [point.x, point.y, 1]
        translateMatrixToCenter = [[1, 0, 0], [0, 1, 0], [-anchorPoint.x, -anchorPoint.y, 1]]
        rotatePoint = numpy.dot(pointMatrix, translateMatrixToCenter)
        rotateMatrix = [[numpy.cos(-Window.angle), -numpy.sin(-Window.angle), 0], [numpy.sin(-Window.angle), numpy.cos(-Window.angle), 0], [0, 0, 1]]
        rotatePoint = numpy.dot(rotatePoint, rotateMatrix)
        translateMatrixBack = [[1, 0, 0], [0, 1, 0], [anchorPoint.x, anchorPoint.y, 1]]
        rotatePoint = numpy.dot(rotatePoint, translateMatrixBack)
        return rotatePoint
