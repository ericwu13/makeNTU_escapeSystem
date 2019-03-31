
from misc import *


class SegmentationMgr:
    def __init__(self, size = (320, 640)):
        self._pointR = (0, 0 , 255)
        self._disR = 250
        self._pointG = (0, 255 , 0)
        self._disG = 280
        self._pointY = (0, 255 , 255)
        self._disY = 350
        self._arrayR = np.array([[self._pointR for i in range(size[1])] for j in range(size[0])])
        self._arrayG = np.array([[self._pointG for i in range(size[1])] for j in range(size[0])])
        self._arrayY = np.array([[self._pointY for i in range(size[1])] for j in range(size[0])])
    def setGraph(self, image, graph):
        res = np.sum(abs(self._arrayR - image), axis = 2) < self._disR
        res |= np.sum(abs(self._arrayG - image), axis = 2) < self._disG
        res |= np.sum(abs(self._arrayY - image), axis = 2) < self._disY
        #  res = res * 255
        for e in graph.edgeL():
            #  print(e.xRange())
            #  print(e.yRange())
            e.setWeight(np.sum(res[e.xRange()[0]:e.xRange()[1], e.yRange()[0]: e.yRange()[1]]))

    


