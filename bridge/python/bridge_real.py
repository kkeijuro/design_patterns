from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "You should implement this."


class PaintTool:
    __metaclass__ = ABCMeta

    @abstractmethod
    def use(self):
        raise Exception(NOT_IMPLEMENTED)


class Furniture:
    __metaclass__ = ABCMeta
    def __init__(self, tool):
        self.tool = tool

    def paint():
        raise Exception(NOT_IMPLEMENTED)


# Painters

class Brush(PaintTool):
    def use(self):    
        print "I paint it with the Brush"

class Spray(PaintTool):
    def use(self):    
        print "I paint it with the Spray"

class Roller(PaintTool):
    def use(self):    
        print "I paint it with the Roller"

# Objects

class Door(Furniture):
    def __init__(self, tool):
        super(Door, self).__init__(tool)

    def paint(self):
        print "I paint the door: ",
        self.tool.use();

class Table(Furniture):
    def __init__(self, tool):
        super(Table, self).__init__(tool)

    def paint(self):
        print "I paint the table: ",
        self.tool.use();

class Chair(Furniture):
    def __init__(self, tool):
        super(Chair, self).__init__(tool)

    def paint(self):
        print "I paint the chair: ",
        self.tool.use();
   
if __name__ == "__main__":
    door = Door(Spray())
    door.paint()
    table = Table(Brush())
    table.paint()
    chair = Chair(Roller())
    chair.paint()
