
from misc import *

class Edge:
    def __init__(self, i):
        self._id = i
        self._vertex = (0,0)
        self._xRange = [0,0]
        self._yRange = [0,0]
        self._weight = 0
    def id(self):
        return self._id
    def vertex(self):
        return self._vertex
    def xRange(self):
        return self._xRange
    def yRange(self):
        return self._yRange
    def otherVertex(self, i):
        if (self._vertex[0] == i):
            return self._vertex[1]
        elif (self._vertex[1] == i):
            return self._vertex[0]
        else:
            assert(false)
    def weight(self):
        return self._weight
    def setVertex(self, i, j):
        self._vertex = (i,j)
    def setX(self, x1, x2):
        self._xRange = [x1,x2]
    def setY(self, y1, y2):
        self._yRange = [y1,y2]
    def setWeight(self, w):
        self._weight = w
