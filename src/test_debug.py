import debug
d=debug.Debug()

def sayFoo():
    print("Foo")

def sayBar():
    print("Bar")

def sayBaz():
    print("Baz")

'''long_string="I did a science project for this article and watched Bird Box, and I have to say I thought it was a mediocre or even below-average film. If I were rating it out of 10, I’d give it a 6. "
long_string+="The pacing was all over the place, the dialogue was laughable (the film features the “joke” “We are making the end of the world … great again! Yoooooooo!” Seriously. I think the dialogue is so bad "
long_string+="that A.I. must have written it.), and the plot of the film was predicated on stupid characters doing stupid things. So as not to be too negative, I will concede that Sandra Bullock had an excellent"
long_string+='performance, and John Malkovich did an excellent job of being a surrogate of my voice in the movie when he asked a character who committed an egregiously stupid act, “Are you a simpleton?"\n'
long_string+="Now, you may be thinking, “Geez, Tucker, you know, maybe you don’t speak for everyone when it comes to watching movies,” and you’d be right. I don’t, nor do I claim to do so. Consider though that the "
long_string+="film boasts a Metacritic score of 52 out of 100 and an audience score on Rotten Tomatoes of 65 percent. Those aren’t stellar enough numbers to equate to 45 million views (Netflix considers those views "
long_string+="to be accounts that watched at least 70 percent of the movie). And yet, here we are in a post-Bird Box world.\n"
long_string+="So how did Netflix pull off the greatest heist of the 21st century? How did they steal two hours from 45 million viewers (3,750,000 days worth of viewing time!!) despite putting out a mediocre movie?"
long_string+=" This is what we keep stressing about great social media presence: it works, and if you do it the right way, it can be free. A significant number of those views came from people simply seeking to "
long_string+=" understand the context of the memes they kept seeing on twitter. Even if the memes originated from less than legitimate accounts, they resulted in millions of legitimate views. That’s"

dictionary1={
        'phone':"iphoneXS",
        'number':"111-111-1111",
        'long string':long_string,
    }

q1="search stack overflow for error?"
q2="would you like to do it again?"
q3="would you like to do it again for the secone time?"

q1_func=sayFoo
q2_func=sayBar
q3_func=sayBaz

dictionary={
        q1_func:{q1:None},
        q2_func:{q2:None},
        q3_func:{q3:None},
    }

dictionary=d.press(feed=dictionary1,tier=2)

for f in dictionary.keys():
    for answer in dictionary[f].values():
        if answer:
            f()
'''
try:
    raise TypeError
except Exception as e:
    print(e)
    print("e.__cause__: "+str(e.__cause__))
    print("e.__class__: "+str(e.__class__))
    print("e.__context__: "+str(e.__context__))
    print("e.__delattr__: "+str(e.__delattr__))
    print("e.__dict__: "+str(e.__dict__))
    print("e.__dir__: "+str(e.__dir__))
    print("e.__doc__: "+str(e.__doc__))
    print("e.__eq__: "+str(e.__eq__))
    print("e.__format__: "+str(e.__format__))
    print("e.__ge__: "+str(e.__ge__))
    print("e.__getattribute__: "+str(e.__getattribute__))
    print("e.__gt__: "+str(e.__gt__))
    print("e.__hash__: "+str(e.__hash__))
    print("e.__init__: "+str(e.__init__))
    print("e.__le__: "+str(e.__le__))
    print("e.__lt__: "+str(e.__lt__))
    print("e.__ne__: "+str(e.__ne__))
    print("e.__new__: "+str(e.__new__))
    print("e.__reduce__: "+str(e.__reduce__))
    print("e.__reduce_ex__: "+str(e.__reduce_ex__))
    print("e.__repr__: "+str(e.__repr__))
    print("e.__setattr__: "+str(e.__setattr__))
    print("e.__setstate__: "+str(e.__setstate__))
    print("e.__sizeof__: "+str(e.__sizeof__))
    print("e.__str__: "+str(e.__str__))
    print("e.__subclasshook__: "+str(e.__subclasshook__))
    print("e.__suppress_context__: "+str(e.__suppress_context__))
    print("e.__traceback__: "+str(e.__traceback__))
