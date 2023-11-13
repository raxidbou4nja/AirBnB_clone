#!/usr/bin/python3
"""
File: Console.py
Path: app/Console.py
Module: Console
Description: simple console application with various states.

--- States ---
    do_quit()
    do_EOF()
    emptyline()
    do_create()
    do_show()
    do_destroy()
    do_all()
    do_count()
    do_update()
    default()
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
        return True

    def do_EOF(self, arg):
        print("")
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
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
        args = shlex.split(arg)
        if args and args[0] not in models.storage.classes:
            print("** class doesn't exist **")
        else:
            instances = [
                str(instance)
                for key, instance in models.storage.all().items()
                if not args or key.split('.')[0] == args[0]
            ]
            print(instances)

    def do_count(self, arg):
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in models.storage.classes:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            count = sum(
                1
                for key in models.storage.all()
                if key.startswith(class_name + ".")
            )
            print(count)

    def do_update(self, arg):
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
            if value[0] == '"' and value[-1] == '"':
                value = value[1:-1]

            if attribute not in ['id', 'created_at', 'updated_at']:
                if not hasattr(instance, attribute):
                    setattr(instance, attribute, None)

                if getattr(instance, attribute) is None:
                    setattr(instance, attribute, value)
                else:
                    setattr(
                        instance,
                        attribute,
                        type(getattr(instance, attribute))(value)
                    )
                instance.save()
            else:
                print("** attribute cannot be updated **")

    def default(self, line):
        pattern_all = r"(\w+)\.all\(\)"
        pattern_count = r"(\w+)\.count\(\)"
        pattern_show = r"(\w+)\.show\([\'\"]?([^\'\"]+)[\'\"]?\)"
        pattern_destroy = r"(\w+)\.destroy\([\'\"]?([^\'\"]+)[\'\"]?\)"
        pattern_update_dict = (
            r'(\w+)\.update\([\'"]?([^\'"]+)[\'"]?,\s*({.*})\)'
        )
        pattern_update_attr = (
            r'(\w+)\.update\('
            r'(?:[\'\"]?([^",]+)[\'\"]?'
            r'(?:\s*,\s*[\'\"]?([^",]+)[\'\"]?)?'
            r'(?:\s*,\s*[\'\"]?([^",]+)[\'\"]?)?)?'
            r'\)'
        )

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
            self.do_update(
                "{} {} {}".format(class_name, instance_id, dict_representation)
            )

        elif match_update_attr:
            class_name = match_update_attr.group(1)
            instance_id = (
                match_update_attr.group(2)
                if match_update_attr.group(2)
                else ""
            )
            attribute_name = (
                match_update_attr.group(3)
                if match_update_attr.group(3)
                else ""
            )
            attribute_value = (
                match_update_attr.group(4)
                if match_update_attr.group(4)
                else ""
            )
            self.do_update(
                "{} {} {} {}".format(
                    class_name, instance_id, attribute_name, attribute_value
                )
            )

        else:
            print("** Unknown syntax: {} **".format(line))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
