import numpy


class Object2D:

    def rotateObject(self, points, anchorPoint, angle):
        objectRotate = []
        for point in points:
            pointMatrix = [point.x, point.y, 1]
            translateMatrixToCenter = [[1, 0, 0], [0, 1, 0], [-anchorPoint.x, -anchorPoint.y, 1]]
            rotatePoint = numpy.dot(pointMatrix, translateMatrixToCenter)
            rotateMatrix = [[numpy.cos(angle), -numpy.sin(angle), 0], [numpy.sin(angle), numpy.cos(angle), 0], [0, 0, 1]]
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
