import numpy
from models.point import Point


class Curve():
    """ A Bezier curve with four control points. """
    def __init__(self, points):
        self.points = self._generate_curve(points)
        self.points.append(points[-1])

    def _generate_curve(self, points):
        def f(t, i):
            operation = numpy.array([t**3, t**2, t, 1])
            operation = operation.dot(numpy.array([
                [-1, 3, -3, 1],
                [3, -6, 3, 0],
                [-3, 3, 0, 0],
                [1, 0, 0, 0],
            ]))

            if i == 0:
                return operation.dot(numpy.array([p.x for p in points]))
            else:
                return operation.dot(numpy.array([p.y for p in points]))

        step = 0.02
        x_points = [f(t, 0) for t in numpy.arange(0, 1+step, step)]
        y_points = [f(t, 1) for t in numpy.arange(0, 1+step, step)]

        coordinates = self.makeCoordinates(x_points, y_points)
        return self.coordinatesToPoint(coordinates)

    def makeCoordinates(self, x_points, y_points):
        coordinates = []
        for i in range(0, len(x_points)):
            coordinates.append([x_points[i], y_points[i]])
        return coordinates

    def coordinatesToPoint(self, points):
        newPoints = []
        for point in points:
            x, y = point
            newPoints.append(Point(x, y))

        return newPoints

# 0,0;0,500;500,500;500,0
# 150,150;150,250;250,300;300,250;300,150;200,100;150,150;150,250;250,300
# 150,150;250,500;300,0;450,720;500,100;550,250;720,500;800,100