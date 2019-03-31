
from path.graph import Graph
from segmentation import *
from stm import *

graph = Graph()
#  segmentationMgr = SegmentationMgr()
#  image = cv2.imread('../data/data1.jpg')
#  segmentationMgr.setGraph(image, graph)
graph.solve()
#  graph.print()
stm = Stm()
stm.configure(graph)


while True:
    string = stm._serial.readline()
    print(string)
