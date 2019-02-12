from selenium.webdriver.chrome.options import Options
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#import debug as bug
from fake_useragent import UserAgent
from selenium import webdriver

class ChromeBrowser:
	def __init__(self,tier,desktop,debug=False):
		#local variables
		self.tier=tier+1
		self.debug=debug
		self.desktop=desktop
		self.width,self.height=self.get_window_dimensions()
		self.useragent=self.get_user_agent()

		#set browser settings
		import os
		self.executable_path=''
		if os.name == 'nt':
			self.executable_path=r'/Users/chadw/Documents/workspace/path/chromedriver.exe'
		else:
			self.executable_path='/home/chad/Documents/workspace/chromedriver/chromedriver'
		print(self.executable_path)
		self.desired_capabilities=self.get_capabilities()
		self.chrome_options=self.get_arguments()

		#initiate driver
		self.driver = webdriver.Chrome(
                    chrome_options=self.chrome_options,
                    #executable_path=self.executable_path,
                    desired_capabilities=self.desired_capabilities,
                    service_args=["--verbose", "--log-path=D:\\qc1.log"],
                )

		#debug statement for browser settings
		if self.debug:
			chrome_settings_dictionary={
					"Browser Specifications":"Driver",
					"executable path":self.executable_path,
					"chrome options":self.chrome_options.to_capabilities(),
					"desired capabilities":self.desired_capabilities,
				}
			self.debug.press(feed=chrome_settings_dictionary,tier=self.tier)

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
			mobile_emulation = { "deviceName": "iPhone 5/SE" }
			chrome_options.add_argument("--user-agent="+str(self.useragent))
			chrome_options.add_argument("--window-size="+str(self.width)+","+str(self.height))
			chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
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
