"""
Bridge pattern example.
"""
from abc import ABCMeta, abstractmethod


NOT_IMPLEMENTED = "You should implement this."


class Drawer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw_circle(self, x, y, radius):
        raise NotImplementedError(NOT_IMPLEMENTED)


class WindowsAPI(Drawer):
    def draw_circle(self, x, y, radius):
        return "API1.circle at {0}:{1} - radius: {2}".format(x, y, radius)


class LinuxAPI(Drawer):
    def draw_circle(self, x, y, radius):
        return "API2.circle at {0}:{1} - radius: {2}".format(x, y, radius)


class Shape:
    __metaclass__ = ABCMeta

    drawing_api = None

    def __init__(self, drawing_api):
        self.drawing_api = drawing_api

    @abstractmethod
    def draw(self):
        raise NotImplementedError(NOT_IMPLEMENTED)

class Circle(Shape):
    def __init__(self, x, y, radius, drawing_api):
        self.x = x
        self.y = y
        self.radius = radius
        super(Circle, self).__init__(drawing_api)

    def draw(self):
        return self.drawing_api.draw_circle(
            self.x, self.y, self.radius
        )

def test():
    shapes = [
        Circle(1.0, 2.0, 3.0, WindowsAPI()),
        Circle(5.0, 7.0, 11.0, LinuxAPI())]
    for shape in shapes:
        print(shape.draw())

if __name__ == "__main__":
    test()
