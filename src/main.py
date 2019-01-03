import spider
import viewport

class Main:
    def __init__(self):
        self.browser = spider.Spider(desktop=False, chrome=True)
        vp = viewport.ViewPort(browser=self.browser)
        self.viewport_dictionary = vp.element_view_dictionary_errors

main = Main()
