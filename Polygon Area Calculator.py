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
       # if isstring(shapewidth) == True:
           # x = str(shapewidth).split('=')
           # shapewidth = x[1]
       # if isstring(shapeheight) == True:
           # y = str(shapeheight).split('=')
           # shapeheight = y[1]
        
        return (self.width * self.height) // (otherpolygon.width * otherpolygon.height)

    def __str__(self):
        if self.__class__.__name__ == 'Rectangle' is True:
            return f'{self.__class__.__name__}(width = {self.width}, height={self.height})'
        else:
           return f'{self.__class__.__name__}(side = {self.width})' 


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

rect = Rectangle(10,5)
print (rect.get_area())
rect.set_height(3)
print (rect.get_perimeter())
print (rect)
print (rect.get_picture())

sq = Square(9)
print (sq.get_area())
sq.set_side(4)
print (sq.get_diagonal())
print (sq)
print (sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print (rect.get_amount_inside(sq))