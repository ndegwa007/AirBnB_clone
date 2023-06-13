#!/usr/bin/python3
"""serializes instances to a JSON file\
        and deserializes JSON file to instances"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Implementation"""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns the dictionary"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """sets in the __objects the obj with key <obj classname>.id"""
        # serializing in this method will make object to be
        # saved without instances
        # suppose u serialize here, you must save
        # immediately inorder to store in the disk
        # FileStorage.__objects[obj.__class__.__name__
        # + '.' + obj.id] = obj.to_dict()
        # instead, store the objects in the
        # FileStorage.__objects and serialize in the save() method
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, 'w') as f:
            new_dict = {
                    k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(new_dict, f)

    def reload(self):
        """
        deserialize the JSON file to __objects
        (only if the JSON file (__file_path) exists)
        if it doesn't do nothing
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                for k, v in (json.load(f)).items():
                    v = eval(v["__class__"])(**v)
                    self.__objects[k] = v
        except Exception:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if in else do nothing"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

#       def get(self, cls, id):
#           """Gets the object associated with id"""
#           item = self.all(cls)
#           for value in item.values():
#               if value.id == id:
#                   return value
#           return None
#
#       def count(self, cls=None):
#           """Counts the number of items of a particular class"""
#           if cls is not None:
#               return len(self.all(cls))
#           return (len(self.all()))
#
    def close(self):
        """deserialize json file to objects"""
        self.reload()
