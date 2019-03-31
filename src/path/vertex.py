
from misc import *
 
class Direction(Enum):
    UP = 0
    DOWN = 1
    RIGHT = 2
    LEFT = 3
    NONE = 4

class Vertex:
    def __init__(self, i):
        self._id = i
        self._edgeL = []
        self._location = [0,0]
        self._dist = []
        self._prev = []
        self._parent = -1
        self._direct = Direction.NONE
        self._light = False
    def id(self):
        return self._id
    def edgeL(self):
        return self._edgeL
    def loaction(self):
        return self._location
    def dist(self):
        return self._dist
    def prev(self):
        return self._prev
    def parent(self):
        return self._parent
    def direct(self):
        return self._direct
    def isLight(self):
        return self._light
    def initializeSSSP(self, n):
        self._dist = [sys.maxsize for i in range(n)]
        self._prev = [None for i in range(n)]
        self._light = False
    def addEdge(self, i):
        self._edgeL.append(i)
    def setLocation(self, x, y):
        self._location = [x,y]
    def setParent(self, id):
        self._parent = id
    def setDirect(self, locate):
        if (self._location == locate):
            self._direct = Direction.NONE
        elif (locate[0] >= self._location[0] and abs(locate[1] - self._location[1]) <= (locate[0] - self._location[0])):
                self._direct = Direction.RIGHT
        elif (locate[0] <= self._location[0] and abs(locate[1] - self._location[1]) <= (self._location[0] - locate[0])):
                self._direct = Direction.LEFT
        elif (locate[1] >= self._location[1] and abs(locate[0] - self._location[0]) <= (locate[1] - self._location[1])):
                self._direct = Direction.DOWN
        elif (locate[1] <= self._location[1] and abs(locate[0] - self._location[0]) <= (self._location[1] - locate[1])):
                self._direct = Direction.UP
        else:
            assert(False);
    def light(self):
        self._light = True


