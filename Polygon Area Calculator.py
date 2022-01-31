from os import name
from sre_compile import isstring

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, number):
        self.width = number

    def set_height(self, number):
        self.height = number

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) **.5)

    def get_picture(self):
        x = ''
        if self.width < 50 or self.height < 50:
            for line in range(self.height):
                x = x + "*" * self.width + '\n'
            return x
        else:
            return 'Too big for picture.'

    def get_amount_inside(self, otherpolygon):
        return (self.width * self.height) // (otherpolygon.width * otherpolygon.height)

    def __str__(self):
        if (self.__class__.__name__ == 'Rectangle') == True:
            return f'{self.__class__.__name__}(width={self.width}, height={self.height})'
        else:
           return f'{self.__class__.__name__}(side={self.width})' 

class Square(Rectangle):
    def __init__(self,side):
        if isstring(side):
            x = str(side).split('=')
            side = x[1]
            self.set_width(side)
            self.set_length(side)
        else:
            self.set_width(side)
            self.set_height(side)

    def set_side(self,number):
        self.side = number
        self.width = number
        self.height = number    