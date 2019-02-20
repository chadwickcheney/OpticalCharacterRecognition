import time
import web
from pprint import pprint
import random
#import debug as bug

class ViewPort:
    def __init__(self,tier,webster,debug,web):
        #local variables
        self.webster=webster

        #debug object
        self.debug=debug
        self.tier=tier+1

        #set local browser for viewport tests
        self.web=web

    #COMMENCE TEST
    def unit_test(self):
        node=self.web.linked_list_all_elements.cur_node
        tests = [self.is_element_obstructed,self.is_element_off_page_partial,self.is_element_off_page_entirely,self.is_element_text_blocked,self.viewport_meta_tag_exists]
        while node:
            for test in tests:
                if test(node):
                    pilot=test.__name__
                    self.web.linked_list_all_elements.add_report(node.selenium_object,pilot)
                    '''if test.__name__ == "viewport_meta_tag_exists":
                        tests.remove(test)'''
            node=node.next

    def is_element_obstructed(self,node):
        if (    (self.is_element_off_page_partial(node) and not self.is_element_off_page_entirely(node)) and
                (not node.element_dictionary['attribute_dictionary']['aria-hidden'])
            ):
            return True
        else:
            return False

    def is_element_off_page_partial(self,node):
        if ( (node.element_dictionary['element_specifications']['x'] < 0 or
                (node.element_dictionary['element_specifications']['x']+node.element_dictionary['element_specifications']['width']) > self.web.client_width)

            or

            (node.element_dictionary['element_specifications']['y'] < 0 or
                (node.element_dictionary['element_specifications']['y']+node.element_dictionary['element_specifications']['height']) > self.web.client_height) ):

            return True
        else:
            return False

    def is_element_off_page_entirely(self,node):
        if ( (node.element_dictionary['element_specifications']['x']+node.element_dictionary['element_specifications']['width']) <= 0 or
                (node.element_dictionary['element_specifications']['x'] >= self.web.client_width)

            or

            (node.element_dictionary['element_specifications']['y']+node.element_dictionary['element_specifications']['height']) <= 0 or
                (node.element_dictionary['element_specifications']['y'] >= self.web.client_height) ):

            return True
        else:
            return False

    def is_element_text_blocked(self, node):
        return False

    def viewport_meta_tag_exists(self, node):
        if 'meta name="viewport" content="width=device-width, initial-scale' in node.element_dictionary['attribute_dictionary']['outerHTML']:
            return True
        return False
