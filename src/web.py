from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from browsers import firefox_browser
from fake_useragent import UserAgent
from browsers import chrome_browser
from selenium import webdriver
import pickle
import time
import sites
from pprint import pprint
import html_element

class Web:
    def __init__(self,tier,webster,debug):
        #local variables
        self.tier=tier+1
        self.driver=None
        self.viewport=None
        self.browser=None
        self.ster=webster
        self.desktop=self.ster.shared_dictionary['desktop']
        self.chrome=self.ster.shared_dictionary['chrome']
        self.debug=debug

        #variables for element_dictionary
        self.avoid_tag_names=["head","html","body","meta","style","link","script","title","noscript","path","polygon"]#what is noscript and should I worry about it
        self.break_tag_names=["head","html","body","meta"]#what is noscript and should I worry about it
        self.css_grab_tags=["color","height","display"]
        self.attribute_grab_tags=["aria-expanded","aria-hidden","outerHTML"]

        #modal test
        self.modal = None

        #determine browser string for debugging
        if self.chrome:
            self.browser="Chrome"
        else:
            self.browser="Firefox"

        #determine viewport string for debugging
        if self.desktop:
            self.viewport='desktop'
        else:
            self.viewport='mobile'

        #initate driver
        if self.chrome:
            self.chrome=chrome_browser.ChromeBrowser(tier,desktop=self.desktop,debug=self.debug)
            self.driver=self.chrome.get_driver()
        else:
            self.firefox=firefox_browser.FirefoxBrowser(tier,desktop=self.desktop,debug=self.debug)
            self.driver=self.firefox.get_driver()

        #client specifications
        self.client_width,self.client_height=self.get_client_specifications()

        #set url
        self.url=self.ster.url

        #go to initial url
        self.go_to(self.url)

        #cookies
        if self.ster.cookies_set:
            self.session_id=webster.session_id
            self.load_cookies,self.save_cookies=self.ster.cookies_set
            self.cookies_file=str(self.url).split('.')[1]+"_"+str(self.session_id)+"_cookies.pkl"
            if self.load_cookies:
                self.load_all_cookies(url=self.url)
                self.go_to(self.url)

        #local storage
        self.linked_list_all_elements=html_element.linked_list(self.debug)

        #get all elements on url page
        self.get_all_elements_on_page()

    def get_client_specifications(self):
        if self.chrome:
            return self.chrome.get_client_specifications()
        else:
            return self.firefox.get_client_specifications()

    def scroll_items_drop_down(self):
        from selenium.webdriver.support.ui import Select
        '''value = "Your desired option's value"
        select_element = Select(driver.find_element_by_tag_name('select')
        for option in select_element.options:
            if option.get_attribute('value') == value:
                select_element.select_by_visible_text(option.text)'''

    def go_to(self, url): #check for modal
        self.driver.get(url)
        def page_has_loaded():
            page_state = self.driver.execute_script(
                'return document.readyState;'
            )
            return page_state == 'complete'
        self.wait_for(page_has_loaded)
        self.check_for_modal()
        self.debug.press(feed="{} has loaded successfully".format(url),tier=self.tier)

    def wait_for(self, condition_function):
        start_time = time.time()
        while time.time() < start_time + 3:
            if condition_function():
                return True
            else:
                time.sleep(0.1)
        raise Exception(
                'Timeout waiting for {}'.format(condition_function.__name__)
            )

    def scroll_element_view(self, element):
        try:
            self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)
        except StaleElementReferenceException as Exception:
            debug.press(feed=str(Exception))

    def get_all_elements_on_page(self):
        elements = self.driver.find_elements_by_xpath("//*[not(*)]")
        for element in elements:
            if not element.tag_name in self.avoid_tag_names:
                self.linked_list_all_elements.add_node(element,element_dictionary=self.get_element_dictionary(element))

        self.linked_list_all_elements.print_specifications()

    def is_attribute(self, element, attribute):
        #verify that its not 100% or auto, etc
        return element.get_attribute(attribute)

    def get_attribute_if_void(self,element,attribute):
        '''if self.is_attribute(element, attribute):
            if 'Features' in element.get_attribute('outerHTML') and element.tag_name == 'a':
                print("attribute found: {}".format(attribute))
                print(element.get_attribute(attribute))
            return element.get_attribute(attribute)
        else:
            parent_element=self.get_parent_of_element(element)

            if 'Features' in element.get_attribute('outerHTML') and element.tag_name == 'a':
                print("searching for attribute: {}".format(attribute))
                print(parent_element.get_attribute('outerHTML'))
                input('>>>')

            if parent_element.tag_name in self.break_tag_names:
                if 'Features' in element.get_attribute('outerHTML') and element.tag_name == 'a':
                    print("Breaking for {}".format(parent.tag_name))
                return False

        return self.get_attribute_if_void(parent_element, attribute)'''


        debug=False
        while True:
            if element.tag_name in self.avoid_tag_names:
                if debug:
                    self.debug.press(feed="broke", tier=self.tier)
                    self.debug.press(feed=element.tag_name, tier=self.tier)
                break
            if element.get_attribute(attribute) == None:
                if debug:
                    self.debug.press(feed="not found", tier=self.tier)
                    self.debug.press(feed=element.get_attribute(attribute), tier=self.tier)
                    self.debug.press(feed=element.get_attribute('outerHTML')[:100], tier=self.tier)
                element = self.get_parent_of_element(element)
            else:
                attr = element.get_attribute(attribute)
                if debug:
                    if 'Features' in element.get_attribute('outerHTML') and element.tag_name == 'a':
                        self.debug.press(feed="Found", tier=self.tier)
                        self.debug.press(feed=attr, tier=self.tier)
                return attr
        return None

    def get_element_dictionary(self, element):
        element_dictionary={}
        #scroll to element
        self.scroll_element_view(element)

        #specs dictionary
        specifications_dictionary = self.driver.execute_script("return arguments[0].getBoundingClientRect()",element)

        css_dict={}
        for tag in self.css_grab_tags:
            css_dict.update({tag:element.get_attribute(tag)})

        attribute_dict={}
        for attribute in self.attribute_grab_tags:
            attribute_dict.update({attribute:self.get_attribute_if_void(element,attribute)})
            '''if 'Features' in element.get_attribute('outerHTML') and element.tag_name == 'a':
                pprint(attribute_dict)
                input('>>>')'''

        element_dictionary.update({'css_dictionary':css_dict})
        element_dictionary.update({'attribute_dictionary':attribute_dict})
        element_dictionary.update({'element_specifications':specifications_dictionary})
        element_dictionary.update({'xpath':self.determine_xpath(element)})

        return element_dictionary

        '''#save to liknked list
        self.linked_list_all_elements.add_node(
                selenium_object=element,
                x=specifications_dictionary['x'],
                y=specifications_dictionary['y'],
                width=specifications_dictionary['width'],
                height=specifications_dictionary['height'],
                outerHTML=element.get_attribute('outerHTML'),
                tag_name=element.tag_name,
                css_property_dictionary=css_dict,
                attribute_dictionary=attribute_dict,
                text=element.text,
            )'''

    def report_test_result(self, selenium_object, pilot):
        self.linked_list_all_elements.add_report(selenium_object, pilot)

    def determine_xpath(self, element):
        tag_names=[]
        while True:
            tag_names.append(element.tag_name)
            element = self.get_parent_of_element(element)
            if element.tag_name == 'html':
                tag_names.append(element.tag_name)
                break
        xpath=''
        for tag in tag_names:
            xpath+=" \ "+str(tag)
        return xpath


    def highlight(self, element):
        """Highlights (blinks) a Selenium Webdriver element"""
        driver = element._parent
        original_style = element.get_attribute('style')
        def apply_new_style(s):
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                    element, s
                )
        def apply_original_style():
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                    element, original_style
                )
        apply_new_style("background: red; border: 10px solid blue;")
        dictionary=self.ster.get_debug_prompt_parameter(
                function_to_call=apply_original_style,
                question_to_ask="Error? (True of False)",
            )
        dictionary=self.debug.press(feed=dictionary, prompt=True,tier=self.tier)
        self.ster.perform_response(dictionary=dictionary)

    def replace_element(self, element):
        next_sibling = driver.execute_script("""
                return arguments[0].nextElementSibling
            """, element)
        return next_sibling

    def get_parent_of_element(self,element):
        return element.find_element_by_xpath('..')

    def load_all_cookies(self,url):
        self.debug.press(feed='Loading cookies for {}'.format(str(str(self.url)+" "+str(self.session_id))),tier=self.tier)
        cookies = pickle.load(open(self.cookies_file,"rb"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
            self.debug.press(feed=str(cookie),tier=self.tier+1)
        self.debug.press(feed='Cookies loaded',tier=self.tier)

    def save_all_cookies(self):
        num=0
        while True:
            num+=1
            print(num)
            try:
                if num>3:
                    raise FileNotFoundError
                pickle.dump(self.driver.get_cookies(),open(self.cookies_file,"wb"))
                break
            except FileNotFoundError:
                file = open(self.cookies_file, "w+")
                file.close()
                self.save_all_cookies()

    def check_for_modal(self):
        return sites.controlledchaorhair_modal(self.driver)
