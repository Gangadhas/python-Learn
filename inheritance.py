# class Polygon:
#     def __init__(self,length):
#         self.length=length
#
#     def __str__(self):
#         return f'polygon with{self.length}sides'
#
#     @property
#     def perimeter(self):
#         print(4*(self.length))
#
# """Finding area and perimeter of a rectangle and square"""
# class Rectangle(Polygon):
#     def __init__(self,height,width):
#         self.height=height
#         self.width=width
#
#     @property
#     def area(self):
#         print(self.height * self.width)
#
# rect=Rectangle(4,5)
# # rect.area
# # print(Polygon)
# # r=Polygon(6)
# rect.perimeter

class Polygon():
    """A class to capture common utilities for dealing with shapes"""

    def __init__(self, side_lengths):
        self.side_lengths = side_lengths

    # def __str__(self):
    #     return 'Polygon with %s sides' % self.num_sides

    @property
    def num_sides(self):
        print(len(self.side_lengths))

    @property
    def perimeter(self):
        print(sum(self.side_lengths))


class Rectangle(Polygon):
    def __init__(self, height, width):
        super().__init__([height, width, height, width])

    @property
    def area(self):
        print(self.side_lengths[0] * self.side_lengths[1])

class Square(Rectangle):
    def __init__(self, height):
        super().__init__(height, height)

r = Rectangle(1, 5)
r.num_sides,r.area, r.perimeter
s = Square(5)
s.num_sides,s.area, s.perimeter
