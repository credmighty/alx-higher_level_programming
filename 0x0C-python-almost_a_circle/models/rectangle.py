#!/usr/bin/python3
"""Module and class Rectangle"""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherits from base imported"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter method"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter method"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter method"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter method"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter method"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter method"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """method area that returns area value of the Rectangle instance."""
        return self.height * self.width

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.width + self.x):
                if j >= self.x:
                    print("#", end="")
                else:
                    print(" ", end='')
            print()

    def __str__(self):
        """by overriding the __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the class Rectangle by adding the public method
        that assigns an argument to each attribute"""

        if args and len(args) != 0:
            for index, value in enumerate(args):
                if index == 0:
                    self.id = value
                elif index == 1:
                    self.width = value
                elif index == 2:
                    self.height = value
                elif index == 3:
                    self.x = value
                elif index == 4:
                    self.y = value
                elif index > 4:
                    raise Exception("Too many arguments")

        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs["id"]
                elif key == "width":
                    self.width = kwargs["width"]
                elif key == "height":
                    self.height = kwargs["height"]
                elif key == "x":
                    self.x = kwargs["x"]
                elif key == "y":
                    self.y = kwargs["y"]

    def to_dictionary(self):
        """returns the dict representation of a rect """
        temp = {}
        temp['id'] = self.id
        temp['width'] = self.width
        temp['height'] = self.height
        temp['x'] = self.x
        temp['y'] = self.y
        return temp
