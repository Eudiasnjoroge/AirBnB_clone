#!/usr/bin/python3
"""module of 'BaseModel' class"""
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Representation of a BaseModel"""
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """class constructor"""
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)

        """Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)

                else:
                    self.__dict__[k] = v
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """custom __str__ method for BaseModel"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                    self.id, self.__dict__))

    def save(self):
        """updates updated_at with the current datetime"""
        self.updated_at = datetime.now()
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
    """returns a dictionary containing all keys/values
        of __dict__ of the instance"""

        dict_ = dict(self.__dict__)
        dict_.update({"__class__": self.__class__.__name__,
                    "created_at":
str(((self.created_at).isoformat())),
                    "updated_at":
str(((self.updated_at).isoformat()))})
        return dict_
        """Return the dictionary of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
