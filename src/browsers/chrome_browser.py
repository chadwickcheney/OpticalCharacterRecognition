from selenium.webdriver.chrome.options import Options
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import user
from fake_useragent import UserAgent
from selenium import webdriver

class ChromeBrowser:
	def __init__(self, shared_dictionary, viewport_num):
		#set variables
		self.viewport=shared_dictionary[viewport_num]
		self.width,self.height=self.get_window_dimensions()
		self.useragent=self.get_user_agent()

		#set browser settings
		self.executable_path='/home/chad/Documents/workspace/chromedriver/chromedriver'
		self.desired_capablities=self.get_capabilities()
		self.chrome_options=self.get_arguments()

		#initiate driver
		self.driver = webdriver.Chrome(
                    chrome_options=self.chrome_options,
                    executable_path=self.executable_path,
                    desired_capabilities=self.desired_capablities,
                    service_args=["--verbose", "--log-path=D:\\qc1.log"],
                )

		#user log to verify window dimensions implicitly
		size=self.driver.get_window_size()
		user.prompt(feed=("Window size: width = {}px, height = {}px.".format(size["width"], size["height"])), notice=True)

	def get_capabilities(self):
		user.prompt(feed='capablilities for {} viewport'.format(self.viewport))
		capabilities={}
		capabilities['name']='selenium test'
		capabilities['resolution']='1920x1080' #test without later
		capabilities['browserstack.debug']='true'
		return capabilities

	def get_arguments(self):
		chrome_options=Options()
		chrome_options.add_argument("--user-agent="+str(self.useragent))
		chrome_options.add_argument("--window-size="+str(self.width)+","+str(self.height))
		return chrome_options


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
