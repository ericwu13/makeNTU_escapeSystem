
from misc import *

class Edge:
    def __init__(self):
        self._vertexL = []
        self._xRange = [0,0]
        self._yRange = [0,0]
        self._weight = 0
    def addVertex(self, i):
        self._vertexL.append(i)
    def setX(self, x1, x2):
        self._xRange = [x1,x2]
    def setY(self, y1, y2):
        self._yRange = [y1,y2]
