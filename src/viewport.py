import time
import web
from pprint import pprint
import random
#import debug as bug
import html_element

class ViewPort:
    def __init__(self,tier,webster,debug,web):
        #local variables
        self.webster=webster
        self.avoid_tag_names=["head","html","body","meta","style","link","script","title","noscript"]#what is noscript and should I worry about it
        self.break_tag_names=["head","html","body","meta"]#what is noscript and should I worry about it
        self.css_grab_tags=["color","height","display"]
        self.attribute_grab_tags=["aria-expanded","aria-hidden"]

        #debug object
        self.debug=debug
        self.tier=tier+1

        #set local browser for viewport tests
        self.web=web

        #get all elements on url page
        self.all_elements=self.web.get_all_elements_on_page()

        #local storage
        self.linked_list_all_elements=html_element.linked_list(self.debug)
        self.linked_list_error_elements=html_element.linked_list(self.debug)

        #setting client specifications
        self.client_width, self.client_height = self.web.get_client_specifications()
        self.debug.press(feed="client width and height from viewport: "+str(self.client_width)+" "+str(self.client_height),tier=self.tier)
        input('>>>')
        
    #COMMENCE TEST
    def unit_test(self):
        #debug statement
        self.debug.press(feed=(('Testing viewport for width:{} | height:{}').format(self.client_width, self.client_height)),tier=self.tier)

        #scan all elements and parse them to verify
        self.scan_elements()
        self.determine_errors()

    def find_width(self, element):
        parent_element=self.web.get_parent_of_element(element)
        if not parent_element.tag_name in self.avoid_tag_names:
            if 'auto' in parent_element.value_of_css_property('width'):
                self.find_width(parent_element)
        else:
            return None

    def is_attribute(self, element, attribute):
        #verify that its not 100% or auto, etc
        return element.get_attribute(attribute)

    def get_attribute_if_void(self,element,attribute):
        if self.is_attribute(element, attribute):
            return element.get_attribute(attribute)
        else:
            parent_element=self.web.get_parent_of_element(element)
            if parent_element.tag_name in self.break_tag_names:
                return False
            else:
                self.get_attribute_if_void(parent_element, attribute)

    def retrieve_elements_specifications(self, element):
        if not element.tag_name in self.avoid_tag_names:
            #scroll to element
            self.web.scroll_element_view(element)

            #specs dictionary
            specifications_dictionary = self.web.driver.execute_script("return arguments[0].getBoundingClientRect()",element)

            css_dict={}
            for tag in self.css_grab_tags:
                css_dict.update({tag:element.get_attribute(tag)})

            self.debug.press(feed=(element.get_attribute('outerHTML')), tier=self.tier)

            attribute_dict={}
            for attribute in self.attribute_grab_tags:
                #self.debug.press(feed=("grabbing attribute "+str(attribute)), tier=self.tier+1)
                attribute_dict.update({attribute:self.get_attribute_if_void(element,attribute)})


            #save to liknked list
            self.linked_list_all_elements.add_node(
                    selenium_object=element,
                    x=specifications_dictionary['x'],
                    y=specifications_dictionary['y'],
                    width=specifications_dictionary['width'],
                    height=specifications_dictionary['height'],
                    outerHTML=element.get_attribute('outerHTML'),
                    tag_name=element.tag_name,
                    css_property_dictionary=css_dict,
                    attribute_dictionary=attribute_dict,
                    text=element.text,
                )

    def scan_elements(self):
        for element in self.all_elements:
            self.retrieve_elements_specifications(element)
        self.linked_list_all_elements.print_specifications()

    #determine what constitutes an error
    def determine_errors(self):
        node=self.linked_list_all_elements.cur_node
        while node:
            if ( (node.x < 0 or (node.x+node.width) > self.client_width) or
                (node.y < 0 or (node.y+node.height) > self.client_height) ):

                self.debug.press(feed='Error found',tier=self.tier)
                dictionary={
                    'x':node.x,
                    'y':node.y,
                    'width':node.width,
                    'height':node.height,
                    'css':node.css_property_dictionary,
                    'tags':node.attribute_dictionary,
                }
                self.debug.press(feed=dictionary, tier=self.tier+2)
                input('>>>')
                self.linked_list_error_elements.add_node(
                        node.selenium_object,
                        node.x,
                        node.y,
                        node.width,
                        node.height,
                        node.outerHTML,
                        node.tag_name,
                        node.css_property_dictionary,
                        node.attribute_dictionary,
                        node.text
                    )
            node=node.next

    def viewport_tag_exists(self):
        for elements in self.all_elements:
            if 'meta name="viewport" content="width=device-width, initial-scale' in str(element.get_attribute('outerHTML')):
                return True
        return False

    def parse_errors(self):
        self.debug.press(feed='Parsing Errors | Will individually hightlight in a blue box and wait for user response',tier=self.tier)
        node=self.linked_list_error_elements.cur_node
        num=0
        while node:
            num+=1
            self.debug.press(feed='parsing errors | {} of {} | {}%'.format(num,self.linked_list_error_elements.get_size(),float(num/self.linked_list_error_elements.get_size())),tier=self.tier+1)
            if node.text:
                output_dictionary={
                        "HTML Element live code":node.outerHTML,
                        "x":node.x,
                        "y":node.y,
                        "TEXT":node.text,
                        "css tags":node.css_property_dictionary,
                        "html object attribute tags":node.attribute_dictionary,
                    }
            else:
                output_dictionary={
                        "HTML Element live code":node.outerHTML,
                        "x":node.x,
                        "y":node.y,
                        "css tags":node.css_property_dictionary,
                        "html object attribute tags":node.attribute_dictionary,
                    }
            self.debug.press(feed=output_dictionary,tier=self.tier)
            self.web.scroll_element_view(node.selenium_object)
            self.web.highlight(node.selenium_object)
            node=node.next
