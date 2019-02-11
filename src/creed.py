import webster
import web as w
import pprint
import debug as bug
import viewport as vp
import response_behavior as rb
import sys
import os

class Main:
    def __init__(self, webster, viewport_num=2):
        #local variables
        self.tier=1
        self.debug=bug.Debug()
        self.webster=webster
        self.web=w.Web(tier=self.tier,webster=self.webster,debug=self.debug)

    def test_units(self):
        #viewport test
        self.viewport=vp.ViewPort(tier=self.tier,webster=self.webster,debug=self.debug,web=self.web)
        self.debug.press(feed='Viewport Test',tier=self.tier)
        self.viewport.unit_test()

        node = self.web.linked_list_all_elements.cur_node
        while node:
            if node.pilot:
                self.web.linked_list_all_elements.print_specifications(node)
            node = node.next
    def debug_error(self,error):
        self.debug.press(feed=error,error=True,tier=0)

def main_function():
    '''try:
        main.test()
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(os.path.split(exc_tb.tb_frame.f_code.co_filename))
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        main.debug.press(feed=(exc_type,fname,exc_tb.tb_lineno),tier=0,error=True)'''
    main.test_units()

webster=webster.Webster()
main = Main(webster=webster)
main_function()
