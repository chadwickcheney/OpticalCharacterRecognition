import time
import web
import pprint
import random
import user
import html_element

class ViewPort:
    def __init__(self,web,url,client):
        #setting url
        self.url=url

        #set local browser for viewport tests
        self.web=web

        #go to url
        self.web.go_to(self.url)

        #get all elements on url page
        self.all_elements=self.web.get_all_elements_on_page()

        #local storage
        self.linked_list_all_elements=html_element.linked_list()
        self.linked_list_error_elements=html_element.linked_list()

        #setting client specifications
        self.client_width, self.client_height = client

    #COMMENCE TEST
    def unit_test(self):
        #debug statement
        user.prompt(feed=(('Testing viewport for width:{} | height{}').format(self.client_width, self.client_height)), tier=3)

        #scan all elements and parse them to verify
        self.scan_elements()
        self.determine_errors()
        self.print_elements_specifications()

    def find_width(self, element):
        parent_element=self.web.get_parent_of_element(element)
        if 'auto' in parent_element.value_of_css_property('width'):
            self.find_width(parent_element)
        else:
            print(parent_element.get_attribute('outerHTML'))
            print(parent_element.value_of_css_property('width'))
            raise TypeError

    def retrieve_elements_specifications(self, element):
        #scroll to element
        self.web.scroll_element_view(element)

        #specs dictionary
        specifications_dictionary = self.web.driver.execute_script("return arguments[0].getBoundingClientRect()",element)

        #parse selenium css properties
        render_width=(str(element.value_of_css_property('width')))
        if 'auto' in render_width:
            print(element.get_attribute('outerHTML'))
            self.find_width(element)
        for i in range(len(render_width)):
            if ord(render_width[i])<48 and ord(render_width[i])>57:
                render_width.replace(render_width[i],'',i)

        print(str("css_property:"+str(element.value_of_css_property('width'))))
        print(str("render_width:"+str(render_width)))

        raise TypeError

        css_dict={
                'css_width':render_width,
                'css_height':(int(element.value_of_css_property('height'))),
                'display':element.value_of_css_property('display'),
            }

        #save to liknked list
        self.linked_list_all_elements.add_node(selenium_object=element,
                x=specifications_dictionary['x'],
                y=specifications_dictionary['y'],
                width=specifications_dictionary['width'],
                height=specifications_dictionary['height'],
                outerHTML=element.get_attribute('outerHTML'),
                tag_name=element.tag_name,
                css_property_dictionary=css_dict,
                text=element.text,
            )

    def scan_elements(self):
        for element in self.all_elements:
            self.retrieve_elements_specifications(element)

    #determine what constitutes an error
    def determine_errors(self):
        node=self.linked_list_all_elements.cur_node
        while node:
            #if node.x < 0 or node.x+width > self.client_width
            node=node.next

    def viewport_tag_exists(self):
        for elements in self.all_elements:
            if 'meta name="viewport" content="width=device-width, initial-scale' in str(element.get_attribute('outerHTML')):
                return True
        return False

    def print_elements_specifications(self):
        self.linked_list_all_elements.print_specifications()
