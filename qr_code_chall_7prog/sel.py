from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib
import urllib.request

driver = webdriver.Firefox(executable_path="Captcha/selenium-firefox/drivers/geckodriver")
website = driver.get('http://challenge01.root-me.org/programmation/ch7/')

#get image
image_url = driver.find_element(by=By.XPATH, value='//img')
image_url = image_url.get_attribute("src")
urllib.request.urlretrieve(image_url, "qr_code_chall_7prog/flash.png")