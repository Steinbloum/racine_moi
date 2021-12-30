import qrcode
import cv2 as cv
import numpy as np
import pandas as pd

# img = qrcode.make('YO THIS IS A TEST')
# img.save('qr_code_chall_7prog/tst.png')

qr =qrcode.QRCode(border=1)
qr.add_data('BAOBAOABAO')
qr.make()
img = qr.make_image()
img.save('qr_code_chall_7prog/tst.png')

# d = cv.QRCodeDetector()
# val, points, straight_qrcode = d.detectAndDecode(cv.imread('qr_code_chall_7prog/flash.png'))
# print(val)
# print(points)
# print(straight_qrcode)

# val, points, straight_qrcode = d.detectAndDecode(cv.imread('qr_code_chall_7prog/tst.png'))
# print(val)
# print(points)
# print(straight_qrcode)

img = cv.imread('qr_code_chall_7prog/flash.png')
img = cv.threshold(img, 127, 255, cv.THRESH_BINARY)[1]
cv.imwrite('qr_code_chall_7prog/flashmod.png', img)
img = cv.imread('qr_code_chall_7prog/flashmod.png')
# df = pd.DataFrame(img, columns=list(lambda x : x for x in range(300)))
print(len(img))
# img = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
border = 0
width = 0
color = 'white'
width = 0 
for x in range(len(img)):
    for y in range(len(img)):
        # print(img[x,y])
        # print(type(img[0,n]))
        comp = img[x,y] == np.array([255,255,255])
        comp = comp.all()
        if comp:
            print("its white")
            if color == 'black':
                continue
            # input()
        else :
            # print('its black')
            # print(f'Coords are [{x}, {y}]')
            if color == 'black':
                width +=1
            else:
                border = x
                color = 'black'
    if border != 0:
        break

print(width)
    
# print(img[0, 0])
# df.append(img)
# print(df)
#top left
width = 8
cv.rectangle(img,(border,border),(width*10,width*10),(0,0,0),-1)
cv.rectangle(img, (border+width, border+width),((width*10)-width, (width*10)-width), (255,255,255),-1 )
cv.rectangle(img,(border+(width*2), (border+(width*2))),((width*10)-(width*2), (width*10)-(width*2)), (0,0,0),-1 )

#bottom left
# border = len(img)-border-(width*10)
# print(border)
# cv.rectangle(img,(border,border),(border+(width*10),border*(width*10)),(0,0,0),-1)
# cv.rectangle(img, (border+width, border+width),((width*10)-width, (width*10)-width), (255,255,255),-1 )
# cv.rectangle(img,(border+(width*2), (border+(width*2))),((width*10)-(width*2), (width*10)-(width*2)), (0,0,0),-1 )

# cv.rectangle(img,(len(img)-border,border),(220,80),(0,0,0),5)
# cv.rectangle(img,(266,34),(236,64),(0,0,0),-1)


cv.imwrite('qr_code_chall_7prog/flashmod.png', img)
d = cv.QRCodeDetector()
val, points, straight_qrcode = d.detectAndDecode(cv.imread('qr_code_chall_7prog/flashmod.png'))
print(val)
print(type(val))
print(points)
# print(straight_qrcode)

val, points, straight_qrcode = d.detectAndDecode(cv.imread('qr_code_chall_7prog/tst.png'))
print(val)
print(points)
# print(straight_qrcode)