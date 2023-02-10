 #!/usr/bin/python3
"""BaseModel Class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel of AirBnB"""
    def __init__(self, *args, **kwargs):
        """initialization of the new BaseModel."""
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = self.created_at
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Current date time implementation"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return dict of BaseModel Instance"""
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """print str representation of BaseModel Instance"""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)1
