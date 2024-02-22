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
    if len(args) < 1:
        print("** class name missing **")
        return
    if args[0] not in self.class_dict:
        print("** class doesn't exist **")
        return
    if len(args) < 2:
        print("** instance id missing **")
        return
    if len(args) < 3:
        print("** attribute name missing **")
        return
    if len(args) < 4:
        print("** value missing **")
        return

    obj_dict = storage.all()
    obj_key = f"{args[0]}.{args[1]}"

    if obj_key not in obj_dict:
        print("** no instance found **")
        return

    obj = obj_dict[obj_key]
    # Prevent updating id, created_at, and updated_at
    if args[2] not in ['id', 'created_at', 'updated_at']:
        attr_value = args[3].strip("\"'")
        # Cast attribute value to int or float if applicable
        try:
            attr_value = int(attr_value)
        except ValueError:
            try:
                attr_value = float(attr_value)
            except ValueError:
                pass
        setattr(obj, args[2], attr_value)
        obj.save()
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
