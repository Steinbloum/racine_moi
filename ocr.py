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
    # img_mod = cv2.blur(img_mod,(5,5))
    # img_mod = cv2.adaptiveThreshold(img_mod, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # img_mod = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # img_mod = cv2.threshold(img_mod, 127, 255, cv2.THRESH_BINARY)[1]
    cv2.imwrite(save_path, img_mod)

# correct_image(path, save_path)