
from misc import *
from path.edge import *
from path.vertex import *
from path.bheap import *

class Graph:
    def __init__(self):
        self.initEdge()
        self.initVertex()
        self.terminal1 = 0;
        self.terminal2 = 0;
        self.terminal3 = 0;
    def initVertex(self):
        vertexNum = 20
        self._vertexL = [Vertex(i) for i in range(vertexNum) ]
        #  self._vertexL[0].addEdge(1)
    def initEdge(self):
        edgeNum = 20
        self._edgeL = [Edge() for i in range(edgeNum) ]
        self._edgeL[0].setX(0,0)
        self._edgeL[0].setY(0,0)
        self._edgeL[0].addVertex(0)

    def singleSourceShortestPath(self, s): 
        # s : source vertex 
        # dist[v] : distance of vertex v to s
        """Compute and return (dist, pred) matrices of computation"""
        pq = BHeap(len(self._vertexL))
        dist = {}
        pred = {}
        
        for v in self._vertexL:
            dist[v.getID()] = sys.maxsize
            pred[v.getID()] = None
        dist[s.getID()] = 0

        for v in self._vertexL:
            pq.insert(v.getID(), dist[v.getID()])

        while not pq.isEmpty():
            u = pq.smallest()
            for edge in self._vertexL[u].edgeL():
                wt = edge.weight()
                newLen = dist[u] + wt

                if newLen < dist[v.getID()]:
                    pq.decreaseKey(v.getID(), newLen)
                    dist[v.getID()] = newLen
                    pred[v.getID()] = u
                    
        return (dist, pred)

    def solution(s, dist, pred):
        if (dist[self.terminal1] <= dist[self.terminal2] && dist[self.terminal1] <= dist[self.terminal3]):
            v = self.terminal1
        else if (dist[self.terminal2] <= dist[self.terminal1] && dist[self.terminal2] <= dist[self.terminal3]):
            v = self.terminal2;
        else if (dist[self.terminal3] <= dist[self.terminal1] && dist[self.terminal3] <= dist[self.terminal2]):
            v = self.terminal3;
        path = [v];
        while v != s:
            v = pred[v]
            path.insert(0, v)
        return path




