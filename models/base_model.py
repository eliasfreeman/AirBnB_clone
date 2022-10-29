#!/usr/bin/python3

import models
import uuid
from datetime import datetime

"""Base Model Class"""


class BaseModel:
    """
        BaseModel Class containing public instance attributes and methods
        This Class defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """Re-creates an instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "__class__":
                    continue
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Prints in the form: [<class name>] (<self.id>) <self.__dict__>"""
        class_name = self.__class__.__name__
        tmp = '[{}] ({}) {}'
        return tmp.format(class_name, self.id, self.__dict__)

    def save(self):
        """
            Updates the public instance attribute (updated_at) with
            current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()
        return

    def to_dict(self):
        """
            Return a dictionary containing all keys/values of the instance
            of __dict__ of the instance with a __class__ entry and
            iso-formatted  datetime
        """
        new_dict = self.__dict__.copy()
        new_dict.update({'__class__': str(self.__class__.__name__)})
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
