from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib
import urllib.request
import pytesseract
from ocr import correct_image
from PIL import Image

tesseract = pytesseract.pytesseract.tesseract_cmd
driver = webdriver.Firefox(executable_path="Captcha/selenium-firefox/drivers/geckodriver")
website = driver.get('http://challenge01.root-me.org/programmation/ch8/')

#get image
image_url = driver.find_element(by=By.XPATH, value='//img')
image_url = image_url.get_attribute("src")
urllib.request.urlretrieve(image_url, "Captcha/img/captcha.png")


#image treatment and text generation :

correct_image('Captcha/img/captcha.png', 'Captcha/img/captcha_mod.png') #From ocr.py
text = pytesseract.image_to_string(Image.open('Captcha/img/captcha_mod.png'))
print(text)
elm = driver.find_element(By.NAME, "cametu")
elm.send_keys(text)
elm.send_keys(Keys.BACKSPACE)
elm.send_keys(Keys.RETURN)

#FUCKING VALIDATED