from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium import webdriver
import user
import time

from browsers import chrome_browser
from browsers import firefox_browser

class Web:
    def __init__(self, chrome=True, desktop=True, debug=False):
        #local variables
        self.driver=None
        self.viewport=None
        self.browser=None
        self.desktop=desktop
        self.debug=debug

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
            self.chrome=chrome_browser.ChromeBrowser(desktop=self.desktop, debug=self.debug)
            self.driver=self.chrome.get_driver()
        '''else:
            firefox=firefox_browser.FirefoxBrowser(desktop=desktop)
            self.driver=firefox.get_driver()'''

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
            user.prompt(feed=str(Exception), notice=True)

    def get_all_elements_on_page(self):
        return self.driver.find_elements_by_xpath("//*[not(*)]")

    def highlight(self, element):
        """Highlights (blinks) a Selenium Webdriver element"""
        driver = element._parent
        def apply_style(s):
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                    element, s
                )
        original_style = element.get_attribute('style')
        apply_style("background: red; border: 5px solid blue;")
        time.sleep(1)
        apply_style(original_style)

    def replace_element(self, element):
        next_sibling = driver.execute_script("""
                return arguments[0].nextElementSibling
            """, element)
        return next_sibling

    def get_parent_of_element(self, element):
        return element.find_element_by_xpath('..')
