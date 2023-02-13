#!/usr/bin/python3
"""
module that serializes instances to a JSON file
and deserializes JSON file to instances
"""

import json
from models.base_model import BaseModel
# from models.user import User


class FileStorage:
    """
    file storage class
    private attributes: __file_path: string-path to the JSON file
                        __objects: dictionary(empty)
    public instance methods:
    all(self): return dictionary __objects
    new(self, obj): sets in __objects to the JSON file
    save(self): serializes __objects to the JSON file
    reload(self): deserializes the JSON file to __objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """ serialize """
        with open(FileStorage.__file_path, "w") as f:
            new_d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(new_d, f)

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
