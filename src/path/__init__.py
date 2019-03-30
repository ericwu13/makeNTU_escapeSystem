
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
        self._objectDetectionMgr.setGraph(image, self._graph)
        self._graph.solve()
        self._stm.configure(self._graph)
