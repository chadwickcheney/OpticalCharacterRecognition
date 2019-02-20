class Webster:
    def __init__(self):
        self.shared_dictionary={
                'desktop':False,
                'chrome':False,
            }
        self.session_id=43

        self.cookies_set=(False, False)

        #self.url='https://www.enginecommerce.com/'
        #self.url='https://www.controlledchaoshair.com/'
        #self.url='http://qualassure.org/#/'
        self.url='https://www.beardedgoat.com'

    def get_debug_prompt_parameter(self, function_to_call, question_to_ask):
        if isinstance(function_to_call, list) and isinstance(question_to_ask, list):
            if len(function_to_call)==len(question_to_ask):
                for i in range(len(function_to_call)):
                    dictionay.update({function_to_call[i]:{question_to_ask[i]:None}})
                return dictionay
            else:
                print("mismatch in lengths of function_to_call and question_to_ask")
                raise TypeError

        elif callable(function_to_call):
            return {function_to_call:{question_to_ask:None}}

        else:
            print("dont know what to tell you")
            raise TypeError

    def perform_response(self,dictionary,params=False):
        for f in dictionary.keys():
            for a in dictionary[f].values():
                if a:
                    if params:
                        f(params)
                    else:
                        f()
