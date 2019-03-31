
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
    def vertexL(self):
        return self._vertexL
    def edgeL(self):
        return self._edgeL
    def setVertex(self):
        vertexNum = 0
        for e in self._edgeL:
            m = max(e.vertex())
            if (m > vertexNum):
                vertexNum = m
        vertexNum += 1
        self._vertexL = [Vertex(i) for i in range(vertexNum) ]
        self._vertexL[0].setLocation(411,94)
        self._vertexL[1].setLocation(578,95)
        self._vertexL[2].setLocation(313,86)
        self._vertexL[3].setLocation(331, 168)
        self._vertexL[4].setLocation(578, 172)
        self._vertexL[5].setLocation(207, 93)
        self._vertexL[6].setLocation(92, 94)
        self._vertexL[7].setLocation(34, 165)
        self._vertexL[8].setLocation(330, 251)
        self._vertexL[9].setLocation(420, 255)
        self._vertexL[10].setLocation(75, 249)
        self._vertexL[11].setLocation(503,35)
        self._vertexL[12].setLocation(148,32)
        self._vertexL[13].setLocation(172, 172)
        self._vertexL[14].setLocation(200, 302)
        self._vertexL[15].setLocation(459,173)
        self._vertexL[16].setLocation(302, 6)
        self._vertexL[17].setLocation(634, 177)
        self._vertexL[18].setLocation(426, 322)

        for e in self._edgeL:
            self._vertexL[e.vertex()[0]].addEdge(e.id())
            self._vertexL[e.vertex()[1]].addEdge(e.id())
        for v in self._vertexL:
            v.edgeL().sort()

    def initEdge(self):
        edgeNum = 25
        self._edgeL = [Edge(i) for i in range(edgeNum) ]
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
        self._edgeL[0].setX(543,630)
        self._edgeL[0].setY(156,195)
        self._edgeL[1].setX(494,636)
        self._edgeL[1].setY(14,66)
        self._edgeL[2].setX(411,580)
        self._edgeL[2].setY(71,112)
        self._edgeL[3].setX(565,632)
        self._edgeL[3].setY(114,158)
        self._edgeL[4].setX(452,555)
        self._edgeL[4].setY(117,230)
        self._edgeL[5].setX(564,629)
        self._edgeL[5].setY(198,274)
        self._edgeL[6].setX(402, 457)
        self._edgeL[6].setY(276,320)
        self._edgeL[7].setX(327,565)
        self._edgeL[7].setY(236,270)
        self._edgeL[8].setX(351,455)
        self._edgeL[8].setY(117,228)
        self._edgeL[9].setX(335,501)
        self._edgeL[9].setY(12,64)
        self._edgeL[10].setX(311,415)
        self._edgeL[10].setY(71,116)
        self._edgeL[11].setX(270,333)
        self._edgeL[11].setY(12,74)
        self._edgeL[12].setX(308,350)
        self._edgeL[12].setY(113,169)
        self._edgeL[13].setX(309,347)
        self._edgeL[13].setY(167,235)
        self._edgeL[14].setX(205,314)
        self._edgeL[14].setY(73,116)
        self._edgeL[15].setX(175,308)
        self._edgeL[15].setY(115,227)
        self._edgeL[16].setX(50,327)
        self._edgeL[16].setY(236,270)
        self._edgeL[17].setX(201,398)
        self._edgeL[17].setY(266,321)
        self._edgeL[18].setX(147,265)
        self._edgeL[18].setY(12,71)
        self._edgeL[19].setX(50,208)
        self._edgeL[19].setY(74,112)
        self._edgeL[20].setX(14,146)
        self._edgeL[20].setY(11,68)
        self._edgeL[21].setX(10,54)
        self._edgeL[21].setY(73,164)
        self._edgeL[22].setX(50,176)
        self._edgeL[22].setY(112,223)
        self._edgeL[23].setX(12,50)
        self._edgeL[23].setY(165,265)
        self._edgeL[24].setX(10, 202)
        self._edgeL[24].setY(267,320)

    def updateEdge(self, data):
        point = np.zeros(640, 320)
        point[data] = 1
        for e in self._edgeL:
            e.setWeight(np.sum(point[e.xRange()[0]:e.xRange()[1], e.yRange()[0]: e.yRange()[1]]))
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
            print("    direct: {}".format(v.direct()))
            print("    isLight: {}".format(v.isLight()))
            #  print("    dist: {}".format(v.dist()))
            #  print("    prev: {}".format(v.prev()))
        #  print("EDGE:")
        #  for e in self._edgeL:
        #      print("  id: {}".format(e.id()))
        #      #  print("    vertex: {}".format(e.vertex()))
        #      print("    weight: {}".format(e.weight()))

