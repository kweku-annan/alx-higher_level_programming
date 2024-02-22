#!/usr/bin/python3
"""Student Module with a class method that retrieves dict representation of
the class's instance"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Instantiates objects with:
        Args:
            first_name(str):
                First name of student
            last_name(str):
                Last name of student
            age(int):
                Age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            filtered_attr = {attr: self.__dict__[attr] for attr in attrs}
            return (filtered_attr)
        else:
            return (self.__dict__)

    def reload_from_json(self, json):
        if json is not None and json != {}:
            self.__dict__ = json
        return (self.__dict__)
