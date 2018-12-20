from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import time

class Spider:
    def __init__(self,desktop=True,chrome=True):
        self.driver = None
        self.viewport = None
        self.useragent = None
        if desktop:
            self.viewport = "Desktop"
            self.useragent = self.get_random_user_agent()
            if chrome:
                self.driver = self.get_desktop_browser(chrome=True)
            else:
                self.driver = self.get_desktop_browser()
            self.set_viewport_size(width=768, height=1280)

        else:
            self.viewport = "Mobile"
            self.useragent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'
            if chrome:
                self.driver = self.get_mobile_browser(chrome=True)
            else:
                self.driver = self.get_mobile_browser()
            self.set_viewport_size(width=320, height=568)

    def get_random_user_agent(self):
        ua = UserAgent()
        return ua.random

    def get_desktop_browser(self, chrome=False):
        if chrome:
            print(str(self.viewport)+"<-viewport | useragent ->"+str(self.useragent))
            opts = Options()
            opts.add_argument("user-agent="+str(self.useragent))
            return webdriver.Chrome(chrome_options=opts, executable_path='C:/Users/chadw/Documents/chromedriver/chromedriver.exe')
        else:
            print(str(self.viewport)+"<-viewport | useragent ->"+str(self.useragent))
            profile = webdriver.FirefoxProfile()
            profile.set_preference("general.useragent.override", self.useragent)
            return webdriver.Firefox(profile)

    def get_mobile_browser(self, chrome=False):
        if chrome:
            print(str(self.viewport)+"<-viewport | useragent ->"+str(self.useragent))
            opts = Options()
            opts.add_argument('--user-agent='+str(self.useragent)+'')
            return webdriver.Chrome(chrome_options=opts, executable_path='C:/Users/chadw/Documents/chromedriver/chromedriver.exe')
        else:
            print(str(self.viewport)+"<-viewport | useragent ->"+str(self.useragent))
            profile = webdriver.FirefoxProfile()
            profile.set_preference("general.useragent.override", str(self.useragent))
            return webdriver.Firefox(profile)

    def set_viewport_size(self, width, height):
        window_size = self.driver.execute_script("""
            return [window.outerWidth - window.innerWidth + arguments[0],
              window.outerHeight - window.innerHeight + arguments[1]];
            """, width, height)
        self.driver.set_window_size(*window_size)

    def options_explore(self):
        '''options.add_argument("--headless") # Runs Chrome in headless mode.
        options.add_argument('--no-sandbox') # Bypass OS security model
        options.add_argument('--disable-gpu')  # applicable to windows os only
        options.add_argument('start-maximized') #
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\path\to\chromedriver.exe')
        driver.get("http://google.com/")'''
