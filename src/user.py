#Local Declarations
width=100

def prompt(feed,options=False,main=True,notice=False,custom=False,custom_space=False,tier=False,type_of=False,test=False,dictionary=False,debug=False):
    if options:
        inter='%'+str(45)+'s'
        for key in feed.keys():
            print(str(inter)%str(key)+" "+str(feed[key]))
    elif notice:
        inter='%'+str(0)+'s'
        print(str(inter)%str(feed))
    elif custom:
        inter='%'+str(int(custom_space))+'s'
        print(str(inter)%str(feed))
    elif tier:
        num_tier = int(str(tier))*10
        inter='%'+str(num_tier)+'s'
        if type_of:
            print(str(inter)%str(type(feed))+" <-type | feed-> "+str(feed))
        else:
            print(str(inter)%str(feed))
    elif test:
        print("__________________________________________________")
        print("##################################################")
        print(feed)
    elif dictionary:
        '''inter_key='%'+str(30)+'s'
        inter_value='%'+str(40)+'s'
        if type(feed) == dict:
            for key in feed.keys():
                print(str(inter_key)%key+" | "+str(feed[key]))
        else:
            print(str(inter_key)%"Not a dictionary")'''
        if type(feed)==dict:
            nested_dictionary_printer(feed)
    elif debug:

    else:
        inter='%'+str(30)+'s'
        print(str(inter)%str(feed))

def get_user_input(string_f=False,int_f=False,feed=False):
    while True:
        if feed:
            prompt(feed, options=bool('dict' in str(type(feed))),notice=bool('str' in str(type(feed))))
        var=input('user: ')
        if string_f:
            var=str(var)
        if int_f:
            var=int(var)
        if int(input('correct?')) == 1:
            return var

def nested_dictionary_printer(dictionary, indent=3):
   for key, value in dictionary.items():
      feed=(str(key))
      inter='%'+str(int(indent)*10)+'s'
      if isinstance(value, dict):
         nested_dictionary_printer(value, indent+1)
      else:
         print(str(inter)%str(feed)+" | "+str(value))

def print_marginalized_string(self, string):
    inter_body='%'+str(25)+'s'
    if isinstance(string, str):
        lines = []
        line=''
        num = 0
        for i in range(len(str(string))):
            line+=string[i]
            if int(i/width) > num:
                print(i/width)
                num += 1
                lines.append(line)
                line=''

    num=0
    for line in lines:
        num+=1
        if num == 1:
            print(str(inter_body)%"BODY: "+str(line))
        else:
            print(str(inter_body)%"|"+str(line))
