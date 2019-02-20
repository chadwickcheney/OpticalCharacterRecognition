from PIL import Image
from io import BytesIO
import pytesseract
import time

class Glasses:
    def __init__(self,web):
        self.web = web
        self.file_name_array = []
        self.num=0

    def is_text_visible(self):
        node = self.web.linked_list_all_elements.cur_node
        while node:
            print(node.selenium_object.text)
            print(self.is_last_lineage(node.selenium_object))
            if node.selenium_object.text and self.is_last_lineage(node.selenium_object):
                print(self.retrive_text_from_image(node, self.make_image(node)))
                print(node.selenium_object.text)
                input('>>> Better or Worse?')
            node = node.next
        self.delete_all_images()

    def is_last_lineage(self, element):
        return element == self.web.get_child_element(element)

    def make_image(self, node):
        self.num+=1
        file_name = 'orc/'+str(self.num)+'.png'
        time.sleep(2)

        self.web.driver.save_screenshot(file_name) # saves screenshot of entire page
        f = file.open(file_name)
        im = Image.open(BytesIO(f)) # uses PIL library to open image in memory
        im = im.crop((
            node.element_dictionary['element_specifications']['x'],
            node.element_dictionary['element_specifications']['y'],
            node.element_dictionary['element_specifications']['x']+
                node.element_dictionary['element_specifications']['width'],
            node.element_dictionary['element_specifications']['y']+
                node.element_dictionary['element_specifications']['height'])
        ) # defines crop points
        im.save(file_name) # saves new cropped image
        time.sleep(2)
        self.file_name_array.append(file_name)

        return file_name

    def retrive_text_from_image(self, node, file_name):
        return pytesseract.image_to_string(Image.open(file_name))

    def delete_all_images(self):
        self.web.debug.press(feed="deleting files", tier=3)
        import os
        for file_name in self.file_name_array:
            cmd = "rm "+str(file_name)
            os.system(cmd)
            self.web.debug.press(feed="deleted {} successfully".format(file_name), tier=4)
            self.web.debug.press(feed="all files deleted successfully", tier=3)
