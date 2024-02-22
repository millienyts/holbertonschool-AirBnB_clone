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
    instance = self.class_dict[args[0]]()
    for attr in args[1:]:
        key, value = attr.split("=")
        setattr(instance, key, self.cast_attr(value))
    instance.save()
    print(instance.id)

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
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.class_dict:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        if arg and arg not in self.class_names:
            print("** class doesn't exist **")
            return
        obj_list = []
        for obj_id in storage.all():
            if not arg or arg == obj_id.split('.')[0]:
                obj_list.append(str(storage.all()[obj_id]))
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.class_names:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        setattr(storage.all()[key], args[2], args[3].strip('"'))
        storage.all()[key].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
