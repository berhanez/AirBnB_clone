#!/usr/bin/python3
"""FileStorage class"""
import json
from models.base_model import BaseModel


class FileStorage:
"""FileStorage Class methods of storage defined.
   Attr's:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Dictionary objects"""
        return self.__objects

    def new(self, obj):
        """set with obj.id"""
        odict = FileStorage.__objects
        ocname = obj.__class__.__name__
        odict["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Obj's serialized to JSON file __file_path"""
   	objdict = {}
        for i, o in FileStorage.__objects.items():
            objdict[i] = o.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)
   
    def reload(self):
        """Deserialize"""
        try:
            with open(FileStorage.__file_path) as f:
                FileStorage.__objects = {}
                objdict = json.load(f)
                for i, o in objdict.items():
                    self.new(BaseModel(**o))                   
        except FileNotFoundError:
            return
