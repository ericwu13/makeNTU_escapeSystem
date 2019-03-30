

from misc import *
from path.graph import *
import serial

class Stm:
    def __init__(self):
        self._serial=serial.Serial("/dev/stdout", 9600, timeout= 0.5 )
    def configure(self, graph):
        self._serial.write("s".encode())
        for v in graph.vertexL():
            self._serial.write("{}".format(v.direct().value).encode())

    

