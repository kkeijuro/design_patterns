class CubeBuilder:
    
    _x = 2
    _y = 3
    _z = 4
    
    def setLength(self, x):
        self._x = x
        return self

    def setHeight(self, y):
        self._y = y
        return self

    def setWidth(self, z):
        self._z = z
        return self
    
    def build(self):
        return Cube(self._x, self._y, self._z)
    
class Cube:

    def __init__(self, h, w, l):
        self._height = h
        self._width = w
        self._length = l
    
    def __str__(self):
        return "Cube Sizes: Height: {0} Width:{1} Length:{2}".format(self._height, self._width, self._length)

if __name__ == '__main__':
    cube = CubeBuilder().setLength(10).setHeight(20).build()
    print cube

