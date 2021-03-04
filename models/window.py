import numpy
from models.world import World
from models.point import Point
from models.object import Object


class Window():
    width = 800
    height = 450
    listObjects = []

    points = [
            (0, height),
            (width, height),
            (width, 0),
            (0, 0),
        ]
    points.append(points[0])

    @staticmethod
    def boundaries():
        return (Window.points[3], Window.points[1])

    @staticmethod
    def angle():
        """ Returns the angle of the 'view up' vector. """
        window_up = numpy.subtract(Window.points[0], Window.points[3])
        return numpy.arctan2(1, 0) - numpy.arctan2(window_up[1], window_up[0])

    @staticmethod
    def center():
        """ Center of the object. """
        x_points = [point[0] for point in set(Window.points)]
        y_points = [point[1] for point in set(Window.points)]
        return (numpy.average(x_points), numpy.average(y_points))

    @staticmethod
    def rotateWindow(angle):
        windowAngle = numpy.radians(angle)
        wcx, wcy = Window.center()
        rotateWindow = [[numpy.cos(windowAngle), -numpy.sin(windowAngle), 0], [numpy.sin(windowAngle), numpy.cos(windowAngle), 0], [0, 0, 1]]
        rotatePoints = []
        for point in Window.points:
            rotatePoint = numpy.array([point[0], point[1], 1])
            x, y, _ = rotatePoint.dot(rotateWindow)
            rotatePoints.append((x, y))
        Window.points = rotatePoints

    @staticmethod
    def move(offSet):
        newPoints = []
        for point in Window.points:
            newPoints.append(tuple(numpy.add(point, offSet)))
        Window.points = newPoints

    @staticmethod
    def zoom(factor):
        # find new window size
        minimum, maximum = Window.boundaries()
        width = maximum[0] - minimum[0]
        height = maximum[1] - minimum[1]

        if width < 10 and height < 10:
            return

        wcx, wcy = Window.center()
        # move object to center
        operation_matrix = numpy.array([
            [1, 0, 0],
            [0, 1, 0],
            [-wcx, -wcy, 1],
        ])

        # perform operation
        operation_matrix = operation_matrix.dot([
            [factor, 0, 0],
            [0, factor, 0],
            [0, 0, 1],
        ])

        # move object back to original position
        operation_matrix = operation_matrix.dot([
            [1, 0, 0],
            [0, 1, 0],
            [wcx, wcy, 1],
        ])

        newPoints = []
        for point in Window.points:
            x, y, _ = numpy.dot(operation_matrix, [point[0], point[1], 1])
            newPoints.append(tuple([x, y]))
        Window.points = newPoints
