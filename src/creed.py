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
        self.client=self.web.get_client_specifications()

    def test(self):
        #viewport test
        self.viewport=vp.ViewPort(tier=self.tier,webster=self.webster,debug=self.debug,web=self.web)
        self.viewport_test()
        #response behavior test
        '''self.response_behavior=rb.ResponseBehavior(tier=self.tier,webster=self.webster,debug=self.debug,web=self.web,url=self.url,client=self.client)
        self.response_behavior_test()'''

    def debug_error(self,error):
        self.debug.press(feed=error,error=True,tier=0)

    def viewport_test(self):
        self.debug.press(feed='Viewport Test',tier=self.tier)
        self.viewport.unit_test()
        dictionary=self.webster.get_debug_prompt_parameter(
                function_to_call=self.viewport.parse_errors,
                question_to_ask="Test Finished | {} errors were found | Would you like to parse through them?".format(self.viewport.linked_list_error_elements.get_size())
            )
        dictionary=self.debug.press(feed=dictionary,prompt=True,tier=self.tier)
        self.webster.perform_response(dictionary=dictionary)

    def response_behavior_test(self):
        self.debug.press(feed='Response Behavior Test',tier=self.tier)
        self.response_behavior.unit_test()

def main_function():
    '''try:
        main.test()
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(os.path.split(exc_tb.tb_frame.f_code.co_filename))
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        main.debug.press(feed=(exc_type,fname,exc_tb.tb_lineno),tier=0,error=True)'''
    main.test()

webster=webster.Webster()
main = Main(webster=webster)
main_function()
