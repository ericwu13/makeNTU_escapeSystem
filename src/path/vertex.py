
from misc import *
 
class Direction(Enum):
    UP = 0
    DOWN = 1
    RIGHT = 2
    LEFT = 3
    NONE = 4

class Vertex:
    def __init__(self):
        self._edgeL = []
        self._loaction = [0,0]
        self._direct = Direction.NONE
        #  self._parent = Vertex()
    def setLocation(self, x, y):
        self._loaction = [x,y]
    def addEdge(self, i):
        self._edgeL.append(i)
