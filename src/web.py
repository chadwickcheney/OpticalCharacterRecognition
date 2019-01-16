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

class Web:
    def __init__(self,tier,webster,chrome=True,desktop=True,debug=False,cookies_set=False):
        #local variables
        self.tier=tier+1
        self.driver=None
        self.viewport=None
        self.browser=None
        self.desktop=desktop
        self.debug=debug
        self.webster=webster

        #determine browser string for debugging
        if chrome:
            self.browser="Chrome"
        else:
            self.browser="Firefox"

        #determine viewport string for debugging
        if desktop:
            self.viewport='desktop'
        else:
            self.viewport='mobile'

        #initate driver
        if chrome:
            self.chrome=chrome_browser.ChromeBrowser(tier,desktop=self.desktop,debug=self.debug)
            self.driver=self.chrome.get_driver()
        else:
            firefox=firefox_browser.FirefoxBrowser(desktop=desktop)
            self.driver=firefox.get_driver()

        #set url
        self.url=webster.shared_dictionary['url']

        #go to initial url
        self.go_to(self.url)

        #cookies
        if cookies_set:
            self.session_id=webster.session_id
            self.load_cookies,self.save_cookies=cookies_set
            self.cookies_file=str(self.url).split('.')[1]+"_"+str(self.session_id)+"_cookies.pkl"
            if self.load_cookies:
                self.load_all_cookies(url=self.url)
                self.go_to(self.url)

    def get_client_specifications(self):
        return self.chrome.get_client_specifications()

    def scroll_items_drop_down(self):
        from selenium.webdriver.support.ui import Select
        '''value = "Your desired option's value"
        select_element = Select(driver.find_element_by_tag_name('select')
        for option in select_element.options:
            if option.get_attribute('value') == value:
                select_element.select_by_visible_text(option.text)'''

    def go_to(self, url):
        self.driver.get(url)
        def page_has_loaded():
            page_state = self.driver.execute_script(
                'return document.readyState;'
            )
            return page_state == 'complete'
        self.wait_for(page_has_loaded)
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
        return self.driver.find_elements_by_xpath("//*[not(*)]")

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
        dictionary=self.webster.get_debug_prompt_parameter(
                function_to_call=apply_original_style,
                question_to_ask="Error? (True of False)",
            )
        dictionary=self.debug.press(feed=dictionary, prompt=True,tier=self.tier)
        self.webster.perform_response(dictionary=dictionary)

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

    '''def check_for_popup_window(self):

    def log_pop_up(self):'''
