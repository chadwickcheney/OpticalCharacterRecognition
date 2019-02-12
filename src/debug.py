from collections import OrderedDict
import selenium

class Debug:
    def __init__(self):
        self.terminal_width,self.terminal_height=(None,None)
        self.horizontal_line=None
        self.horizontal_line_inter=None
        self.tab=10
        self.buffer=40
        self.update(0)

    #only entrance in this classes from other classes
    def press(self,feed,tier,prompt=False,function=False,error=False,new_line_feed=False,trace=False):
        if new_line_feed:
            print("\n")
        else:
            #print horizontal guides
            self.update(tier)
            inter='%'+str(self.tab*tier)+'s'
            print(str(inter)%" "+self.horizontal_line)
            #if need user response
            if prompt:
                if isinstance(feed,dict):
                    for key in feed.keys():
                        for qkey in feed[key].keys():
                            self.print_safe_string(tier,qkey)
                            feed[key].update({qkey:self.get_user_input()})
                    return feed
                if isinstance(feed,str):
                    self.print_safe_string(tier,feed)
                    return self.get_user_input()
            #if not user response needed
            else:
                if error:
                    '''import os
                    for a in feed:
                        cmd = "figlet "+str(a)
                        os.system(cmd)'''
                    self.press(feed=feed,tier=1)

                if trace:
                    print(type(feed))
                    print(len(feed))
                    print(feed)
                    print("\n")
                if isinstance(feed,str):
                    self.print_safe_string(tier=tier,string=feed)
                elif isinstance(feed,dict):
                    self.nested_dictionary_printer(tier,dictionary=feed,trace=trace)
                elif isinstance(feed,list):
                    for f in feed:
                        self.print_safe_string(tier,f)

    #readable error messages and debug statments
    def debug(self, feed):
        self.update()

    def update(self,tier):
        self.terminal_width,self.terminal_height=self.getTerminalSize()
        var=(self.terminal_width-(self.tab*tier))
        self.horizontal_line=("_"*(var))
        self.horizontal_line_inter=("-"*(var))

    #prints infinite nested dictionaries
    def nested_dictionary_printer(self,tier,dictionary,trace=False):
        for key, value in dictionary.items():
            if isinstance(value,dict):
                self.print_safe_string(tier,string=str(key)+" | ")
                self.nested_dictionary_printer(tier+1,value)
            elif isinstance(value,list):
                num=0
                for a in value:
                    num+=1
                    feed=str(key)+" ["+str(num)+"] | "+str(a)
                    self.print_safe_string(tier,string=feed)
            elif isinstance(value,str):
                '''print(type(value))
                print(len(str(value)))
                print((int(self.terminal_width+self.tab+self.buffer)))
                print("tier:"+str(tier))'''
                feed=str(key)+" | "+str(value)
                self.print_safe_string(tier,string=feed,trace=trace)
            else:
                #print("Still come types unaccounted for but we'll send it to {} anwways".format(self.print_safe_string.__name__))
                #print(type(value))
                feed=str(key)+" | "+str(value)
                self.print_safe_string(tier,string=feed)

    #prints string neatly regardless of length
    def print_safe_string(self,tier,string,trace=False):
        extended=self.is_extended(string,tier)
        self.update(tier)
        #establish tab width if specified
        inter='%'+str(self.tab*tier)+'s'
        #print horizontal guides
        print(str(inter)%" "+str(self.horizontal_line_inter))
        #if length of strings (key and value) are greater than width of termanal
        if extended:
            lines=[]
            if isinstance(string, str):
                line=''
                num=0
                for i in range(len(str(string))):
                    #check for ascii codes that are not characters, if not treat as new line feed
                    if ord(string[i])==10 or ord(string[i])==13:
                        lines.append('')
                    #if ascii code is a character, proceed
                    else:
                        #always append line with next character
                        line+=string[i]
                        #if length of incrementing strengh is greater than termanal width
                        #if self.new_line_needed(line,tier,indent):
                        if self.is_extended(line,tier,trace):
                            lines.append(line)
                            if trace:
                                print("Just added {}".format(line))
                                print("lines: {}".format(lines))
                            line=''
            elif isinstance(string, list):
                line=''
                num=0
                for a in string:
                    for i in range(len(str(a))):
                        #check for ascii codes that are not characters, if not treat as new line feed
                        if ord(a[i])==10 or ord(a[i])==13:
                            lines.append('')
                        #if ascii code is a character, proceed
                        else:
                            #always append line with next character
                            line+=a[i]
                            #if length of incrementing strengh is greater than termanal width
                            #if self.new_line_needed(line,tier,indent):
                            if self.is_extended(line,tier):
                                lines.append(line)
                                line=''
            '''#if key is present
            if label:
                num=0
                for line in lines:
                    num+=1
                    if num == 1:
                        print(str(inter)%"key: "+str(label))
                        print(str(inter)%"value: "+str(line))
                    else:
                        print(str(inter)%" | "+str(line))
            #if key is NOT present'''
            for line in lines:
                print(str(inter)%""+str(line))
        #if NOT extended
        else:
            print(str(inter)%""+str(string))

    #scans current termanal at time of call and returns width and heights by character count
    def getTerminalSize(self):
        import os
        env = os.environ
        def ioctl_GWINSZ(fd):
            try:
                import fcntl, termios, struct, os
                cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,
            '1234'))
            except:
                return
            return cr
        cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
        if not cr:
            try:
                fd = os.open(os.ctermid(), os.O_RDONLY)
                cr = ioctl_GWINSZ(fd)
                os.close(fd)
            except:
                pass
        if not cr:
            cr = (env.get('LINES', 25), env.get('COLUMNS', 80))
        return (int(cr[1]), int(cr[0]))

    #get user input
    def get_user_input(self):
        inter='%'+str(self.tab*2)+'s'
        print(str(inter)%"1: True\n"+str(inter)%"2: False\n")
        while True:
            try:
                var=bool(int(input(str(inter)%'user: ')))
                break
            except Exception as e:
                self.press(feed=e,error=True,tier=3)
        return var

    #if string is too long
    def is_extended(self,string,tier,trace=False):
        if len(string)>int((self.terminal_width)+(tier*self.tab)):
            if trace:
                print(string)
                print(len(string))
                print(int((self.terminal_width-self.buffer)-(tier*self.tab)))
                print("\n")
            return True
        return False

    '''def new_line_needed(self,string,tier):
        if (len(str(line))>int(self.terminal_width-self.buffer)-(tier*self.tab)):
            return True
        return False'''
