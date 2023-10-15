#!/usr/bin/env python3
"""The class BaseModel defines all common attributes/methods for other classes"""
from datetime import datetime
import uuid


class BaseModel():
    """Base class for all models"""

    def __init__(self, *args, **kwargs):
        """
            constructor for all models with the given arguments and kwargs
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    def __str__(self):
        """Returns a string representation of class name, id and dictionary
            Arguments: class name and dictionary of class
            Returns: string
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Method to save the time when an update is performed"""
        self.updated_at = datetime.now

    def to_dict(self):
        """Method to returns a dictionary containing all keys/values of __dict__ of the instance
            Arguments: instance (instance of instance)
            Returns: dictionary
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
