#!/usr/bin/env python3
"""contains the entry point of the command interpreter"""


import cmd
from models.basemodel import basemodel

class HBNBCommand(cmd.cmd):
    """takes  cmd.cmd """
    prompt = '(hbnb)'
    def do_eof(self):
        """exits the program"""
        return True

    def quit(self):
        """quits the command to enter the program"""
        return True

    def emptyline(self):
        pass

if __name__ == __main__:
    HBNBCommand.cmdloop()
