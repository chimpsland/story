
import cmd
import os

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""

    def do_greet(self, line):
        print( "hello")

    def do_EOF(self, line):
        return True



class HelloWorld2(cmd.Cmd):
    """Simple command processor example."""

    def do_greet(self, person):
        """greet [person]
        Greet the named person"""
        if person:
            print("hi,", person)
        else:
            print( 'hi')



    def do_list(self, what):
       """
       List current dir.
       """
       print('what: ', what)

       dirs = os.listdir('./')
       for d in dirs:
           print(d)

    def do_EOF(self, line):
        return True

    def postloop(self):
        print


import time
import datetime
seconds = time.time()
d = datetime.datetime.fromtimestamp(seconds)

def show_time():
    seconds = time.time()
    d = datetime.datetime.fromtimestamp(seconds)

    pass



if __name__ == '__main__':
    #HelloWorld().cmdloop()
    #HelloWorld2().cmdloop()

    pass
