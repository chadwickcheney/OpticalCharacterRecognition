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

class Spider:
    def __init__(self,desktop=True,chrome=True):
        self.timeout = 3
        self.driver = None
        self.desktop=desktop
        self.mobile=not desktop
        self.chrome=chrome
        self.viewport=None
        self.useragent=self.get_random_user_agent()
        if self.desktop:
            user.prompt(feed="desktop viewport",notice=True)
            self.viewport='desktop'
        elif self.mobile:
            user.prompt(feed="mobile viewport",notice=True)
            self.viewport='mobile'
        self.driver=self.get_driver()
        self.change_viewport()

    def get_random_user_agent(self):
        if self.mobile:
            return 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'
        else:
            ua = UserAgent()
            return ua.random

    def get_driver(self):
        if self.desktop:
            return self.get_desktop_browser()
        elif self.mobile:
            return self.get_mobile_browser()
        else:
            return None

    def get_desktop_browser(self):
        if self.chrome:
            print(str(self.viewport)+"<-viewport | useragent->"+str(self.useragent))
            opts = Options()
            opts.add_argument("user-agent="+str(self.useragent))
            d = DesiredCapabilities.CHROME
            d['loggingPrefs'] = { 'browser':'ALL' }
            return webdriver.Chrome(
                    chrome_options=opts,
                    executable_path='/home/chad/Documents/workspace/chromedriver/chromedriver',
                    desired_capabilities=self.get_custom_capabilities(),
                    service_args=["--verbose", "--log-path=D:\\qc1.log"],
                )
        else:
            print(str(self.viewport)+"<-viewport | useragent ->"+str(self.useragent))
            profile = webdriver.FirefoxProfile()
            profile.set_preference("general.useragent.override", self.useragent)
            return webdriver.Firefox(profile)

    def get_mobile_browser(self):
        if self.chrome:
            print(str(self.viewport)+"<-viewport | useragent ->"+str(self.useragent))
            opts = Options()
            opts.add_argument('--user-agent='+str(self.useragent)+'')
            chrome_options.add_argument("--window-size=1920,1080")
            return webdriver.Chrome(chrome_options=opts,
                    executable_path='/home/chad/Documents/workspace/chromedriver/chromedriver',
                    desired_capabilities=self.get_custom_capabilities(),
                )
        else:
            print(str(self.viewport)+"<-viewport | useragent ->"+str(self.useragent))
            profile = webdriver.FirefoxProfile()
            profile.set_preference("general.useragent.override", str(self.useragent))
            return webdriver.Firefox(profile)

    def change_viewport(self, width=50, height=50):
        if self.desktop:
            width=1920
            height=1080
        if self.mobile:
            width=320
            height=568
        self.driver.set_window_size(width, height)
        time.sleep(1)
        size=self.driver.get_window_size()
        string=("Window size: width = {}px, height = {}px.".format(size["width"], size["height"]))
        user.prompt(feed=string, notice=True)

    def get_custom_capabilities(self):
        user.prompt(feed="Custom capabilities for {} viewport".format(self.viewport))
        capabilities={}
        capabilities['name']='Selenium Test'
        if self.desktop:
            capabilities['resolution']='1920x1080'
        elif self.mobile:
            capabilities['resolution']='320x568'
            capabilities['browserstack.debug']='true'

    def options_explore(self):
        '''options.add_argument("--headless") # Runs Chrome in headless mode.
        options.add_argument('--no-sandbox') # Bypass OS security model
        options.add_argument('--disable-gpu')  # applicable to windows os only
        options.add_argument('start-maximized') #
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument("--load-images=no")
        driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\path\to\chromedriver.exe')
        driver.get("http://google.com/")'''

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
        apply_style("background: yellow; border: 2px solid red;")
        time.sleep(1)
        apply_style(original_style)

    def replace_element(self, element):
        next_sibling = driver.execute_script("""
                return arguments[0].nextElementSibling
            """, element)
        return next_sibling

    def set_position(self, screen):
        if screen == 1:
            self.driver.set_window_position(0,0)
        elif screen == 2:
            self.driver.set_window_position(1920, 0)
        else:
            return None
