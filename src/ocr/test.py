file_name = 'a.png'
url = ''

from selenium import webdriver
driver = webdriver.Firefox()
driver.get(url)
driver.save_screenshot(file_name)

from PIL import Image
import pytesseract
input('>>> put on glasses')

print(pytesseract.image_to_string(Image.open(file_name)))
