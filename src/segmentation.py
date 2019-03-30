
import numpy as np
import cv2
from segmentation import *

img = cv2.imread('../data/data3.jpg')
#  cv2.waitKey(0)
#  cv2.destroyAllWindows()
#  print(img)
#  print(img.shape)

pointR = (0, 0 , 255)
disR = 250
pointG = (0, 255 , 0)
disG = 280
pointY = (0, 255 , 255)
disY = 350
arrayR = np.array([[pointR for i in range(640)] for j in range(320)])
arrayG = np.array([[pointG for i in range(640)] for j in range(320)])
arrayY = np.array([[pointY for i in range(640)] for j in range(320)])
res = np.sum(abs(arrayR - img), axis = 2) < disR
res |= np.sum(abs(arrayG - img), axis = 2) < disG
res |= np.sum(abs(arrayY - img), axis = 2) < disY
res = res * 255
print(res.shape)
print(res)
#  input()

#  cv2.imshow('image',res)
cv2.imwrite('ans.jpg',res)
#  cv2.waitKey(0)
#  cv2.destroyAllWindows()
#  input()
#  segmentationMgr = SegmentationMgr()
#  segmentationMgr.solve()

