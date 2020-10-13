#!/usr/bin/python3
"""Module to Base"""
import json


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json string"""
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save json str to file"""
        filename = cls.__name__ + ".json"
        Newlist = []
        if list_objs is None:
            cls.to_json_string(list_objs)
        else:
            for a in list_objs:
                Newlist.append(cls.to_dictionary(a))
        with open(filename, "w") as Thefile:
            Thefile.write(cls.to_json_string(Newlist))

    @staticmethod
    def from_json_string(json_string):
        """convert json str to list"""
        thelist = []
        if json_string is None or len(json_string) < 1:
            return thelist
        thelist = json.loads(json_string)
        return thelist

    @classmethod
    def create(cls, **dictionary):
        """return an instance with set attributes"""
        if dictionary is not None and len(dictionary) is not 0:
            if cls.__name__ is "Rectangle":
                dummy = cls(1, 1)
            if cls.__name__ is "Square":
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """return list of instances"""
        Thelist = []
        filename = cls.__name__ + ".json"

        if cls is None:
            return Thelist
        try:
            with open(filename, "r") as Thefile:
                Rdfile = Thefile.read()
                Thelist = cls.from_json_string(Rdfile)
            for a in range(len(Thelist)):
                Thelist[a] = cls.create(**Thelist[a])
        except Exception:
            pass
        return Thelist
