#!/usr/bin/env python3
"""Program that controls the entry point into the command-line."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class that handles the command-line interface."""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Exit the program"""
        return(True)

    def help_quit(self):
        print("Quit command to exit the program")

    def do_EOF(self, line):
        """Exit the command-line interface with EOF(ctrl+D)"""
        print()
        return(True)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
    
