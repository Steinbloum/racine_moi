import pytesseract
import cv2
import numpy as np





# path = 'img/captcha.png'
# save_path = 'img/captcha_mod.png'
tesseract = pytesseract.pytesseract.tesseract_cmd

def correct_image(path, save_path):
    img = cv2.imread(path)
    # img_mod = cv2.resize(img, 300,300)
    black_pixels = np.where(
    (img[:, :, 0] == 0) & 
    (img[:, :, 1] == 0) & 
    (img[:, :, 2] == 0))

# set those pixels to white
    img[black_pixels] = [255, 255, 255]
    img_mod = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(save_path, img_mod)

# correct_image(path, save_path)