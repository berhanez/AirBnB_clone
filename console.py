#!/usr/bin/python3
"""AirBnB console defined."""
import cmd
import models
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


def parse(arg):
    return tuple(arg.split())

class HBNBCommand(cmd.Cmd):
    """ Define AirBnB cmd interpreter.
    Attr's:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """ Do nothing upon receiving an empty line."""
        pass

    def do_create(self, arg):
        """ Create a new BaseModel, print its id, and save it to file.json"""
        arg_tup = parse(arg)
        classes = ["BaseModel", "User"]
        if len(arg_tup) == 0:
            print("** class name missing **")
        elif arg_tup[0] not in classes:
            print("** class doesn't exist **")
        elif arg_tup[0] == classes[0]:
            print(BaseModel().id)
            FileStorage().save()
        elif arg_tup[0] == classes[1]:
            print(BaseModel().id)
            FileStorage().save()
            
    def help_create(self):
        """show information about the create command."""
        print("Usage: create <class>")
        print("Create a new class, print its id, and save it to file.json")

    def do_quit(self, arg):
        """Return upon receiving quit command."""
        return True

    def help_quit(self):
        """show information about the quit command."""
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """Return upon receiving an EOF signal."""
        print("")
        return True

    def help_EOF(self):
        """show information about EOF signal handling."""
        print("EOF signal to exit the program")
    
    def do_show(self, arg):
        """Display string representation of an instance w/ class and id info"""
        arg_tup = parse(arg)
        classes = ["BaseModel", "User"]
        objdict = FileStorage()._FileStorage__objects
        if len(arg_tup) == 0:
            print("** class name missing **")
        elif arg_tup[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg_tup) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_tup[0], arg_tup[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(arg_tup[0], arg_tup[1])])

    def help_show(self):
        """Displays help information for the show command"""
        print("Displays an object's string representation based on the objects class and id")

    def do_destroy(self, arg):
        """Deletes instance based on class name and id updating JSON file"""
        
        arg_tup = parse(arg)
        classes = ["BaseModel", "User"]
        if len(arg_tup) == 0:
            print("** class name missing **")
        elif arg_tup[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg_tup) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_tup[0], arg_tup[1]) not in objdict.keys():
            print("** no instance found**")
        else:
            del objdict["{}.{}".format(arg_tup[0], arg_tup[1])]
            storage.save()

    def help_destroy(self):
        """Display info about destroy command"""
        print("Destroys an object based on id and updates the JSON file")

    def do_all(self, arg):
        """displays string representations of all instances"""
        arg_tup = parse(arg)
        classes = ["BaseModel", "User"]
        if len(arg_tup) > 0 and arg_tup[0] not in classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                objl.append(obj.__str__())
            print(objl)

    def help_all(self):
        """Display help information for the all command"""
        print("Prints a list of string reprs of all instantiated objects")

    def do_update(self, arg):
        """Update instance based on id by adding or updating attribute"""
        arg_tup = parse(arg)
        classes = ["BaseModel", "User"]
        objdict = FileStorage()._FileStorage__objects
        
        if len(arg_tup) == 0:
            print("** class name is missing **")
        elif arg_tup[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg_tup) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_tup[0], arg_tup[1]) not in objdict.keys():
            print("** no instance found **")
        elif len(arg_tup) == 2:
            print("** attribute name missing **")
        elif len(arg_tup) == 3:
            print("** value missing **")
        else:
            obj = objdict["{}.{}".format(arg_tup[0], arg_tup[1])]
            if arg_tup[2] in obj.__dict__.keys():
                valtype = type(obj.__dict__[arg_tup[2]])
                obj.__dict__[arg_tup[2]] = valtype(arg_tup[3])
            else:
                obj.__dict__[arg_tup[2]] = arg_tup[3]
        
        
if __name__ == "__main__":
    HBNBCommand().cmdloop()
