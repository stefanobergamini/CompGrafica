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

    def rotateObject(self, points, anchorPoint, angle):
        objectRotate = []
        rotateAngle = self.getAngleInRadianus(angle)
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

    def scaleObject(self, points, scaleX, scaleY):
        objectScale = []
        cx, cy = self.getCenterObject(points)
        for point in points:
            pointMatrix = [point.x, point.y, 1]
            translateMatrixToCenter = [[1, 0, 0], [0, 1, 0], [-cx, -cy, 1]]
            scalePoint = numpy.dot(pointMatrix, translateMatrixToCenter)
            scaleMatrix = [[scaleX, 0, 0], [0, scaleY, 0], [0, 0, 1]]
            scalePoint = numpy.dot(scalePoint, scaleMatrix)
            translateMatrixBack = [[1, 0, 0], [0, 1, 0], [cx, cy, 1]]
            scalePoint = numpy.dot(scalePoint, translateMatrixBack)
            objectScale.append(scalePoint)
        return objectScale

    def translationObject(self, points, destinationPoint):
        objectTranslation = []
        for point in points:
            pointMatrix = [point.x, point.y, 1]
            translateMatrixToCenter = [[1, 0, 0], [0, 1, 0], [destinationPoint.x, destinationPoint.y, 1]]
            translationPoint = numpy.dot(pointMatrix, translateMatrixToCenter)
            objectTranslation.append(translationPoint)
        return objectTranslation

    def getCenterObject(self, points):
        m = len(points)
        cx = 0
        cy = 0
        for point in points:
            cx += point.x
            cy += point.y
        return [(cx/m), (cy/m)]

    def getAngleInRadianus(self, angle):
        return angle * numpy.pi/180
