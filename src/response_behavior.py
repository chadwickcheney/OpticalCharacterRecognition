class ResponseBehavior:
    def __init__(self,tier,webster,debug,web,client):
        #debug object
        self.debug=debug
        self.tier=tier+1

        #setting url
        self.url=url

        #set local browser for viewport tests
        self.web=web
        self.session_id=webster.session_id

        #go to url
        self.web.go_to(self.url)

        #setting client specifications
        self.client_width, self.client_height=client

        #local variables

    def unit_test(self):
        self.debug.press(feed=(('Testing response behavior for {}'.format(self.url))),tier=self.tier)
        if self.web.save_cookies:
            if self.debug.press(feed='save cookies?',tier=self.tier,prompt=True):
                self.web.save_all_cookies()
