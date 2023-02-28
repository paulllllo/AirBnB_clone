#!/usr/bin/python3
"""A console to handle creation, deletion, updating of objects on website"""
import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the hbnb website"""

    prompt = '(hbnb) '

    def emptyline(self):
        print

    def do_quit(self, line):
        """Exit interpreter"""
        return True

    def do_EOF(self, line):
        """Exit Interpreter"""
        return True



if __name__ == '__main__':
    HBNBCommand().cmdloop()
