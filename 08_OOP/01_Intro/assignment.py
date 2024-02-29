class RightTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height


    def area(self): 
        return 0.5 * self.base * self.height



tri1 = RightTriangle(3,4)
print("the base of tri1 is", tri1.base)
print("the height of tri1 is", tri1.height)
print("the area of tri1 is", tri1.area)