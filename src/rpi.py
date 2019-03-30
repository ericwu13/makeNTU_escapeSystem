
from path import *

rpi = Rpi()
cv2.imwrite("test1.jpg", rpi.query())
cv2.imwrite("test2.jpg", rpi.query())

