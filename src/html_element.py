#----------------------------------------------------------
# NODE STORAGE
#----------------------------------------------------------
class Node:
    def __init__(self,selenium_object,x,y,width,height,outerHTML,tag_name,css_property_dictionary,attribute_dictionary,text=None,test):
        self.selenium_object=selenium_object
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.outerHTML=outerHTML
        self.tag_name=tag_name
        self.css_property_dictionary=css_property_dictionary
        self.attribute_dictionary=attribute_dictionary
        self.text=text
        self.test=test
        self.next = None # contains the reference to the next node

#----------------------------------------------------------
# LINKED LIST STORAGE
#----------------------------------------------------------
class linked_list:
    def __init__(self,debug):
        self.size = 0
        self.cur_node = None
        self.debug=debug

    def add_node(self,selenium_object,x,y,width,height,outerHTML,tag_name,css_property_dictionary,attribute_dictionary,text=None,test=None):
        if len(str(text)) <= 0:
            text=None
        new_node = Node(selenium_object,x,y,width,height,outerHTML,tag_name,css_property_dictionary,attribute_dictionary,text,test) # create a new node
        new_node.next = self.cur_node # link the new node to the 'previous' node.
        self.cur_node = new_node #  set the current node to the new one.
        self.size = self.size + 1

    def get_size(self):
        return self.size

    def print_specifications(self):
        node = self.cur_node
        while node:
            dictionary={
                    'x':node.x,
                    'y':node.y,
                    'width':node.width,
                    'height':node.height,
                    'outerHTML':node.outerHTML,
                    'tag_name':node.tag_name,
                    'css_property_dictionary':node.css_property_dictionary,
                    'attribute_dictionary':node.attribute_dictionary,
                    'text':node.text
                }
            self.debug.press(feed=dictionary,tier=3)
            node=node.next

    def update_element(self, element, pilot):
        node = self.cur_node
        while node:
            if element = node.selenium_object:
                if node.pilot: #if there are results already saved
                    pilot_reports=[]
                    for p in node.pilot:
                        pilot_reports.append(p)
                    pilot_reports.append(pilot)

                    node.pilot=pilot_reports

                else: #first test results for element
                    node.pilot=pilot

                self.print_specifications()

            node=node.next
