#!/usr/bin/python3

""" module uses cmd module """

import cmd


class HBNBCommand(cmd.Cmd):
    """ contains the entry point of the command interpreter """

    prompt = "(hbnb)"

    def do_EOF(self):
        """ exit program """
        return True

    def do_quit(self, args):
        """ Quit command to exit the program \n"""
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
