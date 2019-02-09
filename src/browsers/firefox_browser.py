from selenium.webdriver.chrome.options import Options
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#import debug as bug
from fake_useragent import UserAgent
from selenium import webdriver

class FirefoxBrowser:
	def __init__(self,tier,desktop,debug=False):
		#set variables
		self.desktop=desktop
		self.width,self.height=self.get_window_dimensions()
		self.useragent=self.get_user_agent()
		self.debug=debug
		self.tier=tier

		#set browser settings
		self.profile=self.get_profile()

		#initiate driver
		#self.driver = self.instantiate_driver(self.profile)
		self.driver = webdriver.Firefox(self.profile)
		self.driver.set_window_size(self.width, self.height)

		#user log to verify window dimensions implicitly
		size=self.driver.get_window_size()
		if self.debug:
			firefox_settings_dictionary={
					"Browser Specifications":"Driver",
					"profile":self.profile,
				}
			self.debug.press(feed=firefox_settings_dictionary,tier=self.tier)

	def get_profile(self):
		profile = webdriver.FirefoxProfile()
		profile.set_preference("general.useragent.override", self.useragent)
		return profile

	def instantiate_driver(self, profile):
		capabilities = {
		    'browserName': 'firefox',
		    'firefoxOptions': {
		        'mobileEmulation': {
		            'deviceName': 'iPhone X'
		        }
		    }
		}
		return webdriver.Firefox(desired_capabilities=capabilities)


	def get_window_dimensions(self):
		if self.desktop:
			return (1920,1080)
		else:
			return (320,568)

	def get_user_agent(self):
		if self.desktop:
			ua = UserAgent()
			return ua.random
		else:
			return 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'

	def get_driver(self):
		return self.driver

	def get_client_specifications(self):
		return (self.width, self.height)
