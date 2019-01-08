import dictionary
import web as w
import pprint
import user
import viewport as vp

class Main:
    def __init__(self, shared_dictionary, viewport_num=2):
        #local variables
        self.debug=True
        self.web = w.Web(chrome=shared_dictionary['chrome'], desktop=shared_dictionary['desktop'], debug=self.debug)
        self.client=self.web.get_client_specifications()
        self.url='https://beardedgoat.com/'
        self.viewport=vp.ViewPort(web=self.web,url=self.url,client=self.client)

        #run viewport test
        self.viewport_test()

    def viewport_test(self):
        user.prompt(feed='Viewport Test', test=True)
        self.viewport.unit_test()


d=dictionary.Dictionary()
main = Main(shared_dictionary=d.shared_dictionary)
