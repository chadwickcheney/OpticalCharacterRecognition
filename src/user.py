def prompt(feed,options=False,notice=False,custom=False,custom_space=False,tier=False,type_of=False,test=False):
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
