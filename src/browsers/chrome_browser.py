from selenium.webdriver.chrome.options import Options
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import user
from fake_useragent import UserAgent
from selenium import webdriver

class ChromeBrowser:
	def __init__(self, desktop, debug=False):
		#local variables
		self.desktop=desktop
		self.width,self.height=self.get_window_dimensions()
		self.useragent=self.get_user_agent()

		#set browser settings
		self.executable_path='/home/chad/Documents/workspace/chromedriver/chromedriver'
		self.desired_capabilities=self.get_capabilities()
		self.chrome_options=self.get_arguments()

		#initiate driver
		self.driver = webdriver.Chrome(
                    chrome_options=self.chrome_options,
                    executable_path=self.executable_path,
                    desired_capabilities=self.desired_capabilities,
                    service_args=["--verbose", "--log-path=D:\\qc1.log"],
                )

		#debug statement for browser settings
		if debug:
			user.prompt(feed="Browser Specifications:", tier=2)
			user.prompt(feed=self.executable_path, tier=3)
			user.prompt(feed=self.chrome_options, debug=True)
			user.prompt(feed=self.desired_capabilities, dictionary=True)

		#user log to verify window dimensions implicitly
		size=self.driver.get_window_size()

	def get_capabilities(self):
		capabilities={}
		capabilities['name']='selenium test'
		capabilities['resolution']='1920x1080' #test without later
		#capabilities['resolution']='320x568'
		capabilities['browserstack.debug']='true'
		return capabilities

	def get_arguments(self):
		chrome_options=Options()
		chrome_options.add_argument('disable-infobars')
		if self.desktop:
			chrome_options.add_argument("--user-agent="+str(self.useragent))
		else:
			chrome_options.add_argument("--user-agent="+str(self.useragent))
			#hrome_options.add_experimental_option("mobileEmulation", True)
		chrome_options.add_argument("--window-size="+str(self.width)+","+str(self.height))
		return chrome_options


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
			return '"Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_1_1 like Mac OS X; en) AppleWebKit/534.46.0 (KHTML, like Gecko) CriOS/19.0.1084.60 Mobile/9B206 Safari/7534.48.3"'

	def get_driver(self):
		return self.driver

	def get_client_specifications(self):
		return (self.width, self.height)
