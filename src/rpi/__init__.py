
from misc import *
import picamera

class Rpi:
    def __init__(self):
        self._camera = picamera.PiCamera()
        self._camera.resolution = (640, 320) 
        self._stream = io.BytesIO()
    def query(self):
        self._camera.capture(self._stream, format='jpeg')
        data = np.fromstring(self._stream.getvalue(), dtype=np.uint8)
        image = cv2.imdecode(data, 1)
        return image

    

