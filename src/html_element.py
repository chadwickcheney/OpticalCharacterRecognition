#----------------------------------------------------------
# NODE STORAGE
#----------------------------------------------------------
class Node:
    def __init__(self,selenium_object,element_dictionary,pilot=None):
        self.selenium_object=selenium_object
        self.element_dictionary=element_dictionary
        self.pilot=pilot
        self.next = None # contains the reference to the next node

#----------------------------------------------------------
# LINKED LIST STORAGE
#----------------------------------------------------------
class linked_list:
    def __init__(self,debug):
        self.size = 0
        self.cur_node = None
        self.debug=debug

    def add_node(self,selenium_object,element_dictionary):
        new_node = Node(selenium_object,element_dictionary) # create a new node
        new_node.next = self.cur_node # link the new node to the 'previous' node.
        self.cur_node = new_node #  set the current node to the new one.
        self.size = self.size + 1

    def get_size(self):
        return self.size

    def print_specifications(self,node=None):
        if node:
            self.debug.press(feed=None,tier=None,new_line_feed=True)
            self.debug.press(feed=node.element_dictionary['attribute_dictionary']['outerHTML'],tier=2)
            self.debug.press(feed=node.pilot,tier=3)
            self.debug.press(feed=node.element_dictionary,tier=4)
        else:
            node = self.cur_node
            while node:
                node=node.next

    def add_report(self, selenium_object, pilot):
        node = self.cur_node
        while node:
            if selenium_object == node.selenium_object:
                if node.pilot: #if there are results already saved
                    pilot_reports=[]

                    if isinstance(node.pilot, list):
                        for p in node.pilot:
                            pilot_reports.append(p)
                        pilot_reports.append(pilot)

                    elif isinstance(node.pilot, str):
                        pilot_reports.append(node.pilot)
                        pilot_reports.append(pilot)

                    else:
                        self.debug.press(feed=node.pilot,trace=True)
                        input('handle this type please')

                    print(pilot_reports)
                    node.pilot=pilot_reports

                else: #first test results for element
                    node.pilot=pilot

            node=node.next
