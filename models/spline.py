from models.object import Object
import numpy


class Spline(Object):
    """ A Spline curve with arbitrary amount of control points. """

    def __init__(self, points, color=None, copy=False):
        curve = []
        if(copy):
            curve = points
        else:
            for i in range(len(points) - 3):
                # build a curve for every four control points
                curve += self._generate_curve(points[i:i+4])
        super().__init__(points=curve, type='Curve Spline', color=color, filled=False)

    def _generate_curve(self, points):
        points = self.makeCoordinates(points)
        coef = numpy.multiply(1/6, numpy.array([
            [-1, 3, -3, 1],
            [3, -6, 3, 0],
            [-3, 0, 3, 0],
            [1, 4, 1, 0],
        ])).dot(numpy.array(points))

        number_of_points = 50
        delta = 1/number_of_points
        deltas = numpy.array([
            [0, 0, 0, 1],
            [delta**3, delta**2, delta, 0],
            [6*delta**3, 2*delta**2, 0, 0],
            [6*delta**3, 0, 0, 0],
        ]).dot(coef)

        points = [tuple(deltas[0])]
        for _ in range(number_of_points):
            # update coordinates using forward differences
            deltas[0] += deltas[1]
            deltas[1] += deltas[2]
            deltas[2] += deltas[3]
            points.append(tuple(deltas[0]))
        return self.coordinatesToPoint(points)

    def makeCoordinates(self, points):
        coordinates = []
        for i in range(0, len(points)):
            coordinates.append([points[i].x, points[i].y])
        return coordinates

    def draw(self, painter):
        if self.clip:
            return
        for position in range(0, len(self.points) - 1):
            painter.drawLine(self.points[position], self.points[position+1])