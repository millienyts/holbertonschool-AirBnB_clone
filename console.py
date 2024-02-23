#!/usr/bin/python3
""" This module contains the entry point of the command interpreter."""
import cmd


class HBNBCommand(cmd.Cmd):
    """ Command interpreter class """
    prompt = '(hbnb) '

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt."""
        pass

    def do_EOF(self, line):
        """Exit the program with the shortcut Ctrl+D."""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        """Create command to generate a new instance."""
        if not arg:
            print("** class name missing **")
            return
        print("** Create instance of", arg)

    def do_show(self, arg):
        """Show command to display the string representation of an instance."""
        if not arg:
            print("** class name missing **")
            return
        print("** Show", arg)

    def do_destroy(self, arg):
        """Destroy command to delete an instance."""
        if not arg:
            print("** class name missing **")
            return
        print("** Destroy", arg)

    def do_all(self, arg):
        """All command to display string representation of all instances."""
        if not arg:
            print("** Show all instances **")
        else:
            print("** Show all", arg)

    def do_update(self, arg):
        """Update command to modify an instance."""
        if not arg:
            print("** class name missing **")
            return
        print("** Update", arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
