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
