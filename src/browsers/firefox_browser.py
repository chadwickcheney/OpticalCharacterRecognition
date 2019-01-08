from selenium.webdriver.chrome.options import Options
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import user
from fake_useragent import UserAgent
from selenium import webdriver

class FirefoxBrowser:
	def __init__(self, desktop):
		#set variables
		self.desktop=desktop
		self.width,self.height=self.get_window_dimensions()
		self.useragent=self.get_user_agent()

		#set browser settings
		self.profile=self.get_profile()

		#initiate driver
		self.driver = webdriver.Firefox(self.profile)

		#user log to verify window dimensions implicitly
		size=self.driver.get_window_size()
		user.prompt(feed=("Window size: width = {}px, height = {}px.".format(size["width"], size["height"])), notice=True)

	def get_profile(self):
		profile = webdriver.FirefoxProfile()
		profile.set_preference("general.useragent.override", self.useragent)
		return profile


	def get_window_dimensions(self):
		if self.viewport=='desktop':
			return (1920,1080)
		if self.viewport=='mobile':
			return (320,568)

	def get_user_agent(self):
		if self.viewport=='mobile':
			return 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'
		else:
			ua = UserAgent()
			return ua.random

	def get_driver(self):
		return self.driver
