#!/usr/bin/python3
"""
Entry point for the AirBnB console.
Provides interactive commands for managing the application.
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex  # Used for parsing command arguments

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the AirBnB clone project.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Handle EOF to exit the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty input line."""
        pass

    def do_create(self, arg):
        """Create a new instance of a class, save it, and print the id.
        Usage: create <class name>
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        try:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance based on the class name and id.
        Usage: show <class name> <id>
        """
        args = shlex.split(arg)
        if len(args) < 2:
            print("** class name missing **" if not args else "** instance id missing **")
            return
        try:
            key = f"{args[0]}.{args[1]}"
            print(storage.all()[key])
        except KeyError:
            print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id.
        Usage: destroy <class name> <id>
        """
        args = shlex.split(arg)
        if len(args) < 2:
            print("** class name missing **" if not args else "** instance id missing **")
            return
        try:
            key = f"{args[0]}.{args[1]}"
            del storage.all()[key]
            storage.save()
        except KeyError:
            print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Print all string representations of instances of a class or all classes.
        Usage: all <class name> or all
        """
        args = shlex.split(arg)
        objects = storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
        else:
            try:
                print([str(obj) for key, obj in objects.items() if key.startswith(args[0])])
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on the class name and id.
        Usage: update <class name> <id> <attribute name> <attribute value>
        """
        args = shlex.split(arg)
        if len(args) < 4:
            print("** class name missing **" if not args else
                  "** instance id missing **" if len(args) < 2 else
                  "** attribute name missing **" if len(args) < 3 else
                  "** value missing **")
            return
        try:
            key = f"{args[0]}.{args[1]}"
            obj = storage.all()[key]
            setattr(obj, args[2], eval(args[3]))
            obj.save()
        except KeyError:
            print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
