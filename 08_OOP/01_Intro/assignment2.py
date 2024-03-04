from math import hypot, atan, degrees

class RightTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.small_angle1 = atan(self.height / self.base)
        self.small_angle1 = degrees(self.small_angle1)
        self.large_angle2 = atan(self.base / self.height)
        self.large_angle2 = degrees(self.large_angle2)
        self.small_angle1
    def area(self): 
        return 0.5 * self.base * self.height

    def hypotenuse(self):
        return hypot(self.base, self.height)
    
    def perimeter(self):
        return self.base + self.height + self.hypotenuse()

tri1 = RightTriangle(3,4)
tri2 = RightTriangle(2,3)


print("the perimeter of tri1 is", tri1.perimeter())
print("the hypotenuse of tri1", tri1.hypotenuse())
print("the ares of tri1 is", tri1.area())


print("the height of tri2 is", tri2.height)
print("the area of tri2 is", tri2.area)
print("the base of tri2 is", tri2.base)