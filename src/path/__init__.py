
from misc import *
from path.graph import *
from objectDetection import *
from rpi import *
from segmentation import *
from stm import *

class PathMgr:
    def __init__(self):
        self._rpi = Rpi()
        self._stm = Stm()
        self._graph = Graph()
        self._objectDetectionMgr = ObjectDetectionMgr()
    def solve(self):
        #  while True:
        image = self._rpi.query()
        data = self._objectDetectionMgr.setGraph(image)
        setGraph(data);
        self._graph.solve()
        self._stm.configure(self._graph)
    def setGraph(self, image, data):
        point = np.zeros(640, 320)
        point[data] = 1
        for e in self._graph.edgeL():
            e.setWeight(np.sum(point[e.xRange()[0]:e.xRange()[1], e.yRange()[0]: e.yRange()[1]]))


