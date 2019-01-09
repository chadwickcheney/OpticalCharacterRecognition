class Debug:
    def __init__(self):
        self.terminal_width,self.terminal_height=(None,None)
        self.horizontal_line=None
        self.tab=20
        self.buffer=5
        self.update()

    #only entrance in this classes from other classes
    def press(self,feed,indent=None,prompt=False):
        self.update()
        if prompt:
            print("getting a response from user")
        else:
            if isinstance(feed,str):
                if len(feed) < self.terminal_width:
                    inter=None
                    if indent:
                        inter='%'+str(self.tab*indent)+'s'
                    else:
                        inter='%'+str(self.tab)+'s'
                    print(str(inter)%str(feed))
                else:
                    if indent:
                        self.print_safe_string(feed, indent)
                    else:
                        self.print_safe_string(feed)
            if isinstance(feed,dict):
                self.nested_dictionary_printer(dictionary=feed)

    #readable error messages and debug statments
    def debug(self, feed):
        self.update()

    def update(self):
        self.terminal_width,self.terminal_height=self.getTerminalSize()
        self.horizontal_line=("_"*(self.terminal_width-self.tab))

    def nested_dictionary_printer(self,dictionary,indent=False):
        for key, value in dictionary.items():
            feed=(str(key))
            inter='%'+str(int(indent)*10)+'s'
            if isinstance(value, dict):
                nested_dictionary_printer(value,indent+1)
            else:
                extended_i=False
                if len( str( str(key)+" | "+str(value) ) )>self.terminal_width:
                    extended_i=True
                self.print_safe_string(string=value,label=key,extended=extended_i)

    def print_safe_string(self,string,indent=False,label=False,extended=False):
        #establish tab width if specified
        if indent:
            inter='%'+str(indent)+'s'
        #if not specified
        else:
            inter='%'+str(self.tab)+'s'
        #print horizontal guides
        print(str(inter)%" "+self.horizontal_line)
        #if length of strings (key and value) are greater than width of termanal
        if extended:
            if isinstance(string, str):
                lines=[]
                line=''
                num = 0
                for i in range(len(str(string))):
                    #check for ascii codes that are not characters, if not treat as new line feed
                    if ord(string[i])==10 or ord(string[i])==13:
                        lines.append('')
                    #if ascii code is a character, proceed
                    else:
                        #always append line with next character
                        line+=string[i]
                        #if length of incrementing strengh is greater than termanal width
                        if (len(str(line))+self.buffer)>int(self.terminal_width-self.tab):
                            lines.append(line)
                            line=''
            #if key is present
            if label:
                num=0
                for line in lines:
                    num+=1
                    if num == 1:
                        print(str(inter)%"key: "+str(label))
                        print(str(inter)%"value: "+str(line))
                    else:
                        print(str(inter)%" | "+str(line))
            #if key is NOT present
            else:
                num=0
                for line in lines:
                    num+=1
                    if num == 1:
                        print(str(inter)%"feed: "+str(line))
                    else:
                        print(str(inter)%"|"+str(line))
        #if NOT extended
        else:
            print(str(inter)%str(label)+" | "+str(string))

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
