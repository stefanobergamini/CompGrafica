from models.window import Window


class Viewport():
    xmin = 0
    xmax = 800
    ymin = 0
    ymax = 450
    objects = []

    def transformViewport(self, points):
        listOfPoints = []
        for point in points:
            xvp = ((point.x - Window.xmin) / (Window.xmax - Window.xmin)) * (self.xmax - self.xmin)
            yvp = (1 - ((point.y - Window.ymin) / (Window.ymax - Window.ymin))) * (self.ymax - self.ymin)
            listOfPoints.append([xvp, yvp])
        return listOfPoints