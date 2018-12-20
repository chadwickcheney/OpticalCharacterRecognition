import time
import spider
import pprint

browser = spider.Spider(desktop=False, chrome=True)
time.sleep(1)
driver = browser.driver
driver.get('https://www.enginecommerce.com/')
elements = driver.find_elements_by_xpath("//*[not(*)]")

def element_completely_viewable(driver, elem):
    elem_left_bound = elem.location.get('x')
    elem_top_bound = elem.location.get('y')
    elem_width = elem.size.get('width')
    elem_height = elem.size.get('height')
    elem_right_bound = elem_left_bound + elem_width
    elem_lower_bound = elem_top_bound + elem_height

    win_upper_bound = driver.execute_script('return window.pageYOffset')
    win_left_bound = driver.execute_script('return window.pageXOffset')
    win_width = driver.execute_script('return document.documentElement.clientWidth')
    win_height = driver.execute_script('return document.documentElement.clientHeight')
    win_right_bound = win_left_bound + win_width
    win_lower_bound = win_upper_bound + win_height

    left = bool(win_left_bound<=elem_left_bound)
    right = bool(win_right_bound>=elem_right_bound)
    top = bool(win_upper_bound<=elem_top_bound)
    bottom = bool(win_lower_bound>=elem_lower_bound)

    dict = { 'left':left, 'right':right, 'top':top, 'bottom':bottom }

    return dict

print("Gathering Information")
element_visisbility_dictionary={}
for element in elements:
    dictionary = element_completely_viewable(driver, element)
    element_visisbility_dictionary.update({element:dictionary})

pprint.pprint(element_visisbility_dictionary)

print("Parsing Dictionaries")
for value in element_visisbility_dictionary.items():
    if value['left'] == False or value['right'] == False:
        print("\n############################")
        print("Element not in view")
