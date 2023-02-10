#!/usr/bin/python3
"""AirBnB console defined."""
import cmd
import re
from shlex import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

def parse(arg):
    lexer = shlex(arg)
    retl = [i.strip(",") for i in lexer]
    return retl

class HBNBCommand(cmd.Cmd):
    """ Define AirBnB cmd interpreter.
    Attr's:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """ Does nothing upon receiving an empty line."""
        pass
        
    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argl = arg.split('.')
        command = argl[1].split('(')
        command[1] = command[1].strip(')')
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        if command[0] in argdict.keys():
            return argdict[command[0]]("{} {}".format(argl[0], command[1]))
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Return upon receiving quit command."""
        return True


    def do_EOF(self, arg):
        """Return upon receiving an EOF signal(exit)."""
        print("")
        return True
    
    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and prints its id.
        """
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()
            
    def do_show(self, arg):
        """Display string representation of an instance w/ class and id info
        Usage:show <class> <id>"""
        argl = parse(arg)
        objdict = storage.all()
        
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """Deletes instance based on class name and id updating JSON file
        Usage: destroy <class> <id>"""
        argl = parse(arg)
        objdict = storage.all()
        
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found**")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """displays string representations of all instances
        Usage: all <class>"""
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)
            
    def do_count(self, arg):
        """Retrieve the number of instances of a given class.
        Usage: count <class>"""
        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Update instance based on id by adding or updating attribute.
        Usage: update <class> <id> <attribute_name> <attribute_value>"""
        argl = parse(arg)
        objdict = storage.all()
        
        if len(argl) == 0:
            print("** class name is missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
        elif len(argl) == 2:
            print("** attribute name missing **")
        elif len(argl) == 3 and type(eval(arg[2])) != dict::
            print("** value missing **")
        elif len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__dict__.keys():
                valtype = type(obj.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(arg[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(arg[2]).items():
                if k in obj.__dict__.keys():
                    valtype = type(obj.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        
if __name__ == "__main__":
    HBNBCommand().cmdloop()
