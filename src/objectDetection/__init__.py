# from misc import *
import os

class ObjectDetectionMgr:
    def __init__(self):
        pass
    def setGraph(self, image, graph):
        os.system("scp -P 50035 image.jpg pwhuang@eda.ee.ntu.edu.tw:/home/pwhuang/")
        os.system("ssh pwhuang@eda.ee.ntu.edu.tw -p 50035 'bash -s' < exe.sh")
        os.system("scp -P 50035 pwhuang@eda.ee.ntu.edu.tw:pos.npy .")

if __name__ == "__main__":
    os.system("scp -P 50035 image.jpg pwhuang@eda.ee.ntu.edu.tw:/home/pwhuang/")
    os.system("ssh pwhuang@eda.ee.ntu.edu.tw -p 50035 'bash -s' < exe.sh")
    os.system("scp -P 50035 pwhuang@eda.ee.ntu.edu.tw:pos.npy .")
    pass

