#!/usr/bin/python3
# coding: utf-8

import pytesseract
import os
import argparse
from PIL import Image, ImageOps, ImageEnhance
from htmlextractor import Htmlator
import cv2
import numpy as np
from ocr import correct_image


# imgpath = 'img/testcapt.png'
tesseract = pytesseract.pytesseract.tesseract_cmd
h = Htmlator()

# def solve_captcha(path):

#     """
#     Convert a captcha image into a text,
#     using PyTesseract Python-wrapper for Tesseract
#     Arguments:
#         path (str):
#             path to the image to be processed
#     Return:
#         'textualized' image
#     """
#     image = Image.open(path).convert('RGB')
#     image = ImageOps.autocontrast(image)

#     filename = "{}.png".format(os.getpid())
#     image.save(filename)

#     text = pytesseract.image_to_string(Image.open(filename))
#     return text


# if __name__ == '__main__':
#     argparser = argparse.ArgumentParser()
#     argparser.add_argument("-i", "--image", required=True, help="img/testcapt.png")
#     args = vars(argparser.parse_args())
#     path = args["image"]
#     print('-- Resolving')
#     captcha_text = solve_captcha(path)
#     print('-- Result: {}'.format(captcha_text))
raw = h.extract_html("http://challenge01.root-me.org/programmation/ch8/")
idx = raw.find('<img src="')
start_index = idx + len('<img src="')
end_index = raw.find('" /><br><br><')
result = raw[start_index:end_index]

imgpt = h.save_img_from_url(result, "Captcha/img/captcha.png")
# img = cv2.imread("Captcha/img/captcha.png")
# img_mod = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.medianBlur(img_mod,5)
# cv2.threshold(img_mod, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
# cv2.imwrite('Captcha/img/captcha_mod.png', img_mod)


# img = Image.open(img)
# img = cv2.cvtColor(imgpt, cv2.COLOR_BGR2GRAY)

correct_image('Captcha/img/captcha.png', 'Captcha/img/captcha_mod.png')
text = pytesseract.image_to_string(Image.open('Captcha/img/captcha_mod.png'))
print(text)
