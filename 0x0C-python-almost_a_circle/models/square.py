#!/usr/bin/python3
"""Module for Square class inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from base imported"""

    def __init__(self, size, x=0, y=0, id=None):
        """square initializer"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """by overriding the __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """get the size method"""
        return self.width

    @size.setter
    def size(self, value):
        """width setter method"""
        self.width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Update the class Square by adding the public method
        that assigns an argument to each attribute"""

        if args and len(args) != 0:
            for index, value in enumerate(args):
                if index == 0:
                    self.id = value
                elif index == 1:
                    self.size = value
                elif index == 2:
                    self.x = value
                elif index == 3:
                    self.y = value
                elif index >= 4:
                    raise Exception("Too many arguments")

        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs["id"]
                elif key == "size":
                    self.size = kwargs["size"]
                elif key == "x":
                    self.x = kwargs["x"]
                elif key == "y":
                    self.y = kwargs["y"]

    def to_dictionary(self):
        """returns the dict representation of a sqr"""
        temp = {}
        temp['id'] = self.id
        temp['size'] = self.size
        temp['x'] = self.x
        temp['y'] = self.y
        return temp
