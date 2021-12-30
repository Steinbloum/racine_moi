import qrcode
import cv2 as cv

img = qrcode.make('YO THIS IS A TEST')
img.save('qr_code_chall_7prog/tst.png')



d = cv.QRCodeDetector()
val, points, straight_qrcode = d.detectAndDecode(cv.imread('qr_code_chall_7prog/flash.png'))
print(val)

val, points, straight_qrcode = d.detectAndDecode(cv.imread('qr_code_chall_7prog/tst.png'))
print(val)
