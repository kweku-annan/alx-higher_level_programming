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

    def to_json(self):
        return (self.__dict__)
