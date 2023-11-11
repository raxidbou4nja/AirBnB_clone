#!/usr/bin/python3
"""
Console Module
"""
import cmd
import shlex
import models
from models.base_model import BaseModel
import datetime
import re

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF"""
        print("")  # Print a new line for better formatting
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in models.storage.classes:
            print("** class doesn't exist **")
        else:
            new_instance = models.storage.classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in models.storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                print(models.storage.all()[key])

    def do_count(self, arg):
        """Count the number of instances of a class"""
        class_name = arg
        if class_name not in models.__dict__:
            print("** class doesn't exist **")
            return
        count = sum(1 for key in models.storage.all() if key.startswith(class_name + "."))
        print(count)


    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in models.storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = shlex.split(arg)
        if args and args[0] not in models.storage.classes:
            print("** class doesn't exist **")
        else:
            instances = [str(instance) for key, instance in models.storage.all().items() if not args or key.split('.')[0] == args[0]]
            print(instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in models.storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in models.storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instance = models.storage.all()[key]
            attribute = args[2]
            value = args[3]
            if hasattr(instance, attribute) and attribute not in ['id', 'created_at', 'updated_at']:
                setattr(instance, attribute, type(getattr(instance, attribute))(value))
                instance.save()
            else:
                print("** attribute doesn't exist or cannot be updated **")

    def default(self, line):
        """Called on an unrecognized command."""
        pattern = r"(\w+)\.(\w+)\(.*\)"
        match = re.match(pattern, line)
        if match:
            class_name = match.group(1)
            method_name = match.group(2)
            if method_name == "all":
                self.do_all(class_name)
            if method_name == "count":
                self.do_count(class_name)
        else:
            print("** Unknown syntax: {} **".format(line))

if __name__ == '__main__':
    HBNBCommand().cmdloop()