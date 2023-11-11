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

    def do_count(self, arg):
        """Count the number of instances of a class"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in models.storage.classes:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            count = sum(1 for key in models.storage.all() if key.startswith(class_name + "."))
            print(count)


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

            # Extracting the value, handling spaces in string arguments
            value = args[3]
            if value[0] == '"' and value[-1] == '"':
                value = value[1:-1]

            if hasattr(instance, attribute) and attribute not in ['id', 'created_at', 'updated_at']:
                # Only update if the attribute exists and is not one of the restricted ones
                setattr(instance, attribute, type(getattr(instance, attribute))(value))
                instance.save()
            else:
                print("** attribute doesn't exist or cannot be updated **")


    def default(self, line):
        """Called on an unrecognized command."""
        pattern_all = r"(\w+)\.all\(\)"
        pattern_count = r"(\w+)\.count\(\)"
        pattern_show = r"(\w+)\.show\([\'\"]?([^\'\"]+)[\'\"]?\)"
        pattern_destroy = r"(\w+)\.destroy\([\'\"]?([^\'\"]+)[\'\"]?\)"
        pattern_update_dict = r'(\w+)\.update\([\'"]?([^\'"]+)[\'"]?,\s*({.*})\)'
        pattern_update_attr = r'(\w+)\.update\((?:[\'\"]?([^",]+)[\'\"]?(?:\s*,\s*[\'\"]?([^",]+)[\'\"]?)?(?:\s*,\s*[\'\"]?([^",]+)[\'\"]?)?)?\)'

        match_all = re.match(pattern_all, line)
        match_count = re.match(pattern_count, line)
        match_show = re.match(pattern_show, line)
        match_destroy = re.match(pattern_destroy, line)
        match_update_dict = re.match(pattern_update_dict, line)
        match_update_attr = re.match(pattern_update_attr, line)

        if match_all:
            class_name = match_all.group(1)
            self.do_all("{}".format(class_name))

        elif match_count:
            class_name = match_count.group(1)
            self.do_count("{}".format(class_name))

        elif match_show:
            class_name = match_show.group(1)
            instance_id = match_show.group(2)
            self.do_show("{} {}".format(class_name, instance_id))

        elif match_destroy:
            class_name = match_destroy.group(1)
            instance_id = match_destroy.group(2)
            self.do_destroy("{} {}".format(class_name, instance_id))


        elif match_update_dict:
            class_name = match_update_dict.group(1)
            instance_id = match_update_dict.group(2)
            dict_representation = match_update_dict.group(3)
            self.do_update("{} {} {}".format(class_name, instance_id, dict_representation))


        elif match_update_attr:
            class_name = match_update_attr.group(1)
            instance_id = match_update_attr.group(2) if match_update_attr.group(2) else ""
            attribute_name = match_update_attr.group(3) if match_update_attr.group(3) else ""
            attribute_value = match_update_attr.group(4) if match_update_attr.group(4) else ""
            self.do_update("{} {} {} {}".format(class_name, instance_id, attribute_name, attribute_value))


        else:
            print("** Unknown syntax: {} **".format(line))

if __name__ == '__main__':
    HBNBCommand().cmdloop()