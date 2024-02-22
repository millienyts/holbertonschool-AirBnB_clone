#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    class_dict = {
        'BaseModel': BaseModel,
        'User': User
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.class_dict:
            print("** class doesn't exist **")
            return
        
        new_instance = self.class_dict[args[0]]()
        new_instance.save()
        print(new_instance.id)


    def cast_attr(self, value):
        """Attempts to cast `value` to an int, float, or leave as string."""
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value.strip('"').replace('_', ' ')

    def do_show(self, arg):
        """Shows an instance based on class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] in self.class_dict:
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = f"{args[0]}.{args[1]}"
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        args = arg.split()
        if len(args) < 2:
            print("** class name missing **" if len(args) == 0 else "** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")
                
    def do_all(self, arg):
        args = arg.split()
        if len(args) > 0 and args[0] not in self.class_dict:
            print("** class doesn't exist **")
            return
        obj_list = [str(obj) for key, obj in storage.all().items() if not args or key.startswith(args[0])]
        print(obj_list)
def do_update(self, arg):
    args = arg.split()
    if len(args) < 4:
        print("** class name missing **" if len(args) == 0 else
              "** instance id missing **" if len(args) == 1 else
              "** attribute name missing **" if len(args) == 2 else
              "** value missing **")
        return
    key = f"{args[0]}.{args[1]}"
    if key in storage.all():
        setattr(storage.all()[key], args[2], args[3].strip('"'))
        storage.all()[key].save()
    else:
        print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
