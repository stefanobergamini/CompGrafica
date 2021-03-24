from models.object import Object
import numpy


class Curve(Object):
    """ A Bezier curve with four control points. """

    def __init__(self, points, color=None, copy=False):
        if(copy):
            curve = points
        else:
            curve = self._generate_curve(points)
            curve.append(points[-1])
        super().__init__(points=curve, type='Curve Bezier', color=color, filled=False)

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

    def draw(self, painter):
        if self.clip:
            return
        for position in range(0, len(self.points) - 1):
            painter.drawLine(self.points[position], self.points[position+1])

# 0,0;0,500;500,500;500,0
# 150,150;150,250;250,300;300,250;300,150;200,100;150,150;150,250;250,300
# 150,150;250,500;300,0;450,720;500,100;550,250;720,500;800,100