import cv2 as cv
import numpy as np


class QR_reparator():
    def __init__(self, url) -> None:
        self.url = url
        self.img = cv.imread(self.url)
        self.imgmod = cv.threshold(self.img, 127, 255, cv.THRESH_BINARY)[1]
        self.border = self.find_border()

    def make_corners(self, border, width):
        width = 8
        cv.rectangle(self.imgmod,(border,border),(width*10,width*10),(0,0,0),-1)
        cv.rectangle(self.imgmod, (border+width, border+width),((width*10)-width, (width*10)-width), (255,255,255),-1 )
        cv.rectangle(self.imgmod,(border+(width*2), (border+(width*2))),((width*10)-(width*2), (width*10)-(width*2)), (0,0,0),-1 )
        self.save('qr_code_chall_7prog/flashmod.png', self.imgmod)

    def save(self, url, img):
        cv.imwrite(url, img)

    def find_border(self):
        border = 0
        for x in range(len(self.imgmod)):
            for y in range(len(self.imgmod)):
                # print(f'{x} {y}')
                # print(self.imgmod[x, y])
                comp = self.imgmod[x,y] == np.array([255,255,255])
                comp = comp.all()
                if comp:
                    pass
                else :
                    border = x
                    break
            if border != 0:
                break
        return x

qr=QR_reparator("qr_code_chall_7prog/flash.png")
# print(qr.read_qr())
print(qr.border)
qr.make_corners(qr.border, 8, len(qr.img))