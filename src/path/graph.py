
from misc import *
from path.edge import *
from path.vertex import *

class Graph:
    def __init__(self):
        self.initEdge()
        self.initVertex()
    def initVertex(self):
        vertexNum = 20
        self._vertexL = [Vertex() for i in range(vertexNum) ]
        #  self._vertexL[0].addEdge(1)
    def initEdge(self):
        edgeNum = 20
        self._edgeL = [Edge() for i in range(edgeNum) ]
        self._edgeL[0].setX(0,0)
        self._edgeL[0].setY(0,0)
        self._edgeL[0].addVertex(0)


