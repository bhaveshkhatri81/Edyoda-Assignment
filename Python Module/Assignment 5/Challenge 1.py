# Challenge 1: Square Numbers and Return Their Sum

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return print("The Square of the number ", self.x, self.y, self.z, "is",self.x**2 + self.y**2 + self.z**2)


point = Point(2, 3, 4)

result = point.sqSum()