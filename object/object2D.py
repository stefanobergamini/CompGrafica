from windows.viewport import Viewport
from windows.window import Window


class Object2D:
    def transformViewport(self, point):
        x = ((point.x - Window.xmin) / (Window.xmax - Window.xmin)) * \
            (Viewport.xmax - Viewport.xmin)
        y = (1 - ((point.y - Window.ymin) / (Window.ymax - Window.ymin))
             ) * (Viewport.ymax - Viewport.ymin)
        return (x, y)
