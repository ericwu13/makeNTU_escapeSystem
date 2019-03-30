
from misc import *
from path.edge import *
from path.vertex import *
from path.bheap import *

class Graph:
    def __init__(self):
        self.initEdge()
        self.setVertex()
        self.simpleInit()
        self._terminal = [16, 17, 18];
        self._lightThreshold = 2
    def setVertex(self):
        vertexNum = 0
        for e in self._edgeL:
            m = max(e.vertex())
            if (m > vertexNum):
                vertexNum = m
        vertexNum += 1

        self._vertexL = [Vertex(i) for i in range(vertexNum) ]
        for e in self._edgeL:
            self._vertexL[e.vertex()[0]].addEdge(e.id())
            self._vertexL[e.vertex()[1]].addEdge(e.id())
        for v in self._vertexL:
            v.edgeL().sort()

    def initEdge(self):
        edgeNum = 25
        self._edgeL = [Edge(i) for i in range(edgeNum) ]
        #  self._edgeL[0].setX(0,0)
        #  self._edgeL[0].setY(0,0)
        self._edgeL[0].setVertex(4,17)
        self._edgeL[1].setVertex(1,11)
        self._edgeL[2].setVertex(0,1)
        self._edgeL[3].setVertex(1,4)
        self._edgeL[4].setVertex(4,15)
        self._edgeL[5].setVertex(4,9)
        self._edgeL[6].setVertex(9,18)
        self._edgeL[7].setVertex(8,9)
        self._edgeL[8].setVertex(3,15)
        self._edgeL[9].setVertex(0,11)
        self._edgeL[10].setVertex(0,2)
        self._edgeL[11].setVertex(2,16)
        self._edgeL[12].setVertex(2,3)
        self._edgeL[13].setVertex(3,8)
        self._edgeL[14].setVertex(2,5)
        self._edgeL[15].setVertex(3,13)
        self._edgeL[16].setVertex(8,10)
        self._edgeL[17].setVertex(8,14)
        self._edgeL[18].setVertex(5,12)
        self._edgeL[19].setVertex(5,6)
        self._edgeL[20].setVertex(6,12)
        self._edgeL[21].setVertex(6,7)
        self._edgeL[22].setVertex(7,13)
        self._edgeL[23].setVertex(7,10)
        self._edgeL[24].setVertex(10,14)

    def simpleInit(self):
        for e in self._edgeL:
            e.setWeight(1)
        self._edgeL[18].setWeight(5)
    def singleSourceShortestPath(self, i): 
        # s : source vertex 
        # dist[v] : distance of vertex v to s
        """Compute and return (dist, pred) matrices of computation"""
        pq = BHeap(len(self._vertexL))
        
        s = self._vertexL[self._terminal[i]]
        #  print(s.dist())
        s.dist()[i] = 0
        s.prev()[i] = self._terminal[i]

        for v in self._vertexL:
            pq.insert(v.id(), v.dist()[i])

        while not pq.isEmpty():
            currentV = pq.smallest()
            #  print("current vertex: {}".format(currentV));
            for edge in self._vertexL[currentV].edgeL():
                wt = self._edgeL[edge].weight()
                newLen = self._vertexL[currentV].dist()[i] + wt

                newV = self._edgeL[edge].otherVertex(currentV)

                if (newLen < self._vertexL[newV].dist()[i]):
                    pq.decreaseKey(newV, newLen)
                    #  print("update")
                    #  print("new vertex: {}".format(newV))
                    #  print("vertex 2 prev: {}".format(self._vertexL[2].prev()))
                    self._vertexL[newV].dist()[i] = newLen
                    self._vertexL[newV].prev()[i] = currentV

    def solve(self):
        for v in self._vertexL:
            v.initializeSSSP(len(self._terminal))
        for i in range(len(self._terminal)):
            self.singleSourceShortestPath(i)

        for v in self._vertexL:
            id = np.argmin(np.array(v.dist()))
            #  print(v.dist())
            #  print(v.prev())
            #  print(id)
            v.setParent(v.prev()[id])
            v.setDirect(self._vertexL[v.prev()[id]].loaction())
        for e in self._edgeL:
            if (e.weight() <= self._lightThreshold):
                continue
            #  print("edge: {}".format(e.id()))
            if self._vertexL[e.vertex()[0]].parent() == e.vertex()[1]:
                v = e.vertex()[0]
            elif self._vertexL[e.vertex()[1]].parent() == e.vertex()[0]:
                v = e.vertex()[1]
            else:
                v = e.vertex()[0]
            #  print("v: {}".format(v))
            while (self._vertexL[v].parent() != v):
                self._vertexL[v].light()
                v = self._vertexL[v].parent()

    def print(self):
        print("VERTEX:")
        for v in self._vertexL:
            print("  id: {}".format(v.id()))
            #  print("    edge: {}".format(v.edgeL()))
            print("    parent: {}".format(v.parent()))
            print("    isLight: {}".format(v.isLight()))
            #  print("    dist: {}".format(v.dist()))
            #  print("    prev: {}".format(v.prev()))
        #  print("EDGE:\n")
        #  for e in self._edgeL:
        #      print("  id: {}".format(e.id()))
        #      print("    vertex: {}".format(e.vertex()))

