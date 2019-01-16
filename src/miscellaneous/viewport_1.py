import spider
import time
import pprint
import random
import user

class ViewPort:
    def __init__(self, browser=None, url=None):
        self.url=None
        if url:
            self.url = url
        else:
            self.url_list = [
                    'https://www.enginecommerce.com/',
                    'https://www.starbucks.com/',
                    'https://www.amazon.com/',
                    'https://www.beardedgoat.com/'
                ]
            self.url = (self.url_list[random.randint(0,len(self.url_list)-1)])

        #set local browser for viewport tests
        self.browser = browser

        #go to url
        self.browser.go_to(self.url)

        #get all elements on url page
        self.all_elements = self.browser.get_all_elements_on_page()

        #local variables for test and results
        self.element_view_dictionary_errors = {}
        self.element_view_dictionary = {}

        #scan all elements and parse them to verify
        self.scan_elements()
        self.parse_errors()

    def element_completely_viewable(self, driver, elem):
        #scroll to element
        self.browser.scroll_element_view(elem)

        #get elements specs
        elem_left_bound = elem.location.get('x')
        elem_top_bound = elem.location.get('y')
        elem_width = elem.size.get('width')
        elem_height = elem.size.get('height')
        elem_right_bound = elem_left_bound + elem_width
        elem_lower_bound = elem_top_bound + elem_height

        #get window specs
        win_width = driver.execute_script('return document.documentElement.clientWidth')
        win_height = driver.execute_script('return document.documentElement.clientHeight')
        win_upper_bound = driver.execute_script('return window.pageYOffset')
        win_lower_bound = win_upper_bound + win_height
        win_left_bound = driver.execute_script('return window.pageXOffset')
        win_right_bound = win_left_bound + win_width

        top=bool(win_upper_bound<=elem_top_bound)
        bottom=bool(win_lower_bound>=elem_lower_bound)
        left=bool(win_left_bound<=elem_left_bound)
        right=bool(win_right_bound>=elem_right_bound)

        dictionary={
                'top':top_dictionary,
                'bottom':bottom_dictionary,
                'left':left_dictionary,
                'right':right_dictionary
            }

        return dictionary

    def scan_elements(self):
        for element in self.all_elements:
            #user.prompt(feed=element.get_attribute('innerHTML'), tier=2)
            self.element_view_dictionary.update({element:dict(self.element_completely_viewable(self.browser.driver, element))})

        #Check results
        for key in self.element_view_dictionary.keys():
            for dimension_key in self.element_view_dictionary[key].keys():
                if self.element_view_dictionary[key][dimension_key] == False:
                    self.element_view_dictionary_errors.update({key:self.element_view_dictionary[key]})
        input('length: ' +str(len(self.element_view_dictionary_errors))+str(' >>> '))

    def parse_errors(self):
        #Need to determine if element is collapsed in a dropdown menu
        #Tag name, css elements, has 'button' in elment children, etc...
        #Tap targets
        for element in self.element_view_dictionary_errors.keys():
            self.browser.scroll_element_view(element)
            self.browser.highlight(element)
            user.prompt(feed=element.get_attribute('outerHTML'), tier=3)
            pprint.pprint(self.element_view_dictionary_errors[element])
            input('>>>')

    def viewport_tag(self):
        for elements in self.all_elements:
            if 'meta name="viewport" content="width=device-width, initial-scale' in str(element.get_attribute('outerHTML')):
                return True
        return False
