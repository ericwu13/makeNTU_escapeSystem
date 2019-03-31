
from objectDetection import *
from path.graph import Graph

graph = Graph()
objectDetectionMgr = ObjectDetectionMgr()
img = cv2.imread('../data/data7.jpg')
data = objectDetectionMgr.setGraph(img)
graph.updateEdge(data)
graph.print()

