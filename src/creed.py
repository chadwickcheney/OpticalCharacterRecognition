from browsers import chrome_browser
from browsers import firefox_browser
import dictionary
import web
import pprint
import user

class Main:
    def __init__(self, shared_dictionary, chrome=True, viewport_num=1):
        #get shared dictionary
        self.shared_dictionary=shared_dictionary

        #variables
        self.viewport=self.shared_dictionary[viewport_num]
        self.driver=None
        self.browser=None
        if chrome:
            self.browser="Chrome"
        else:
            self.browser="Firefox"

        #get driver for tests
        if chrome:
            chrome=chrome_browser.ChromeBrowser(self.shared_dictionary, viewport_num)
            self.driver=chrome.driver
        else:
            firefox=firefox_browser.FirefoxBrowser(self.shared_dictionary, viewport_num)
            self.driver=firefox.driver

        #run viewport test
        self.viewport_test()

        def viewport_test(self):
            user.prompt(feed=('Running Viewport Test on {} with {} window size'.format(self.browser,self.viewport)), test=True)

d=dictionary.Dictionary()
main = Main(shared_dictionary=d.shared_dictionary)
