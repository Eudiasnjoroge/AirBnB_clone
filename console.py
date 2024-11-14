#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB clone"""
    prompt = "(hbnb)"

    def do_create(self, arg):
        """Create a new instance of a specified class"""
        if not arg:
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            obj = storage.classes()[arg]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Show an instance based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            obj = storage.all().get(key)
            if obj:
                print(obj)
            else:
                print("** no instance found **")

    def do_quit(self, arg):
        """Quit the console"""
        return True

    def do_EOF(self, arg):
        """End-of-file command to exit the console"""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
