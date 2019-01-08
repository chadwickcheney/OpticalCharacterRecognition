class Debug:
    def __init__(self):
        self.tab=20
        self.terminal_width,self.terminal_height=self.getTerminalSize()

    def prompt(self, feed, indent=None):
        self.terminal_width,self.terminal_height=self.getTerminalSize()
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

    def debug(self, feed):
        self.terminal_width,self.terminal_height=self.getTerminalSize()

    def error_message(self, feed):
        self.terminal_width,self.terminal_height=self.getTerminalSize()

    def nested_dictionary_printer(self, dictionary, indent=False):
        for key, value in dictionary.items():
            feed=(str(key))
            inter='%'+str(int(indent)*10)+'s'
            if isinstance(value, dict):
                nested_dictionary_printer(value, indent+1)
            else:
                extended_i=False
                if len( str( str(key)+" | "+str(value) ) )>self.terminal_width:
                    extended_i=True
                self.print_safe_string(string=value,label=key,extended=extended_i)

    def print_safe_string(self, string, indent=False, label=False, extended=True):
        print("##############")
        if extended:
            if indent:
                inter_body='%'+str(indent)+'s'
            else:
                inter_body='%'+str(self.tab)+'s'
            if isinstance(string, str):
                lines=[]
                line=''
                num = 0
                for i in range(len(str(string))):
                    line+=string[i]
                    """if indent:
                        if int(i/(self.terminal_width)) > num:
                            #print(i/self.terminal_width)
                            num += 1
                            lines.append(line)
                            line=''
                    else:
                        if int(i/(self.terminal_width)) > num:
                            print(i/self.terminal_width)
                            num += 1
                            lines.append(line)
                            line=''"""
                    if len(str(line))>int(self.terminal_width-self.tab):
                        print(type(lines))
                        print(type(line))
                        lines.append(line)
                        print(line)
                        lines=''
            if label:
                num=0
                for line in lines:
                    num+=1
                    if num == 1:
                        print(str(inter_body)%"key: "+str(label))
                        print(str(inter_body)%"value: "+str(line))
                    else:
                        print(str(inter_body)%"|"+str(line))
            else:
                num=0
                for line in lines:
                    num+=1
                    if num == 1:
                        print(str(inter_body)%"feed: "+str(line))
                    else:
                        print(str(inter_body)%"|"+str(line))
        else:
            if indent:
                inter='%'+str(indent)+'s'
            else:
                inter='%'+str(self.tab)+'s'
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
