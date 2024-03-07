class Rectangle:

    counter = 0
    
    def get_count():
        return Rectangle.get_count

    def __init__(self, base: float, height: float) -> None:
        self.__base = base
        self.__height = height
        
    def get_height(self) -> float:
        return self.__height
    
    def get_base(self) -> float:
        return self.__base
    
    def get_perimeter(self) -> float:
        return 2 * self.__base + 2 * self.__height
    
    def get_area(self) -> float:
        return 2 * self.__base + 2 * self.__height
 
 
rectangle1 = Rectangle(3.0, 4.0)

print("the base is " , rectangle1.get_base)
print("the height is", rectangle1.get_height)
print("the perimeter is", rectangle1.get_perimeter)
print("the area is", rectangle1.get_area)

Rectangle2 = Rectangle(4.0, 3.0)
print("the base is " , Rectangle2.get_base)
print("the height is", Rectangle2.get_height)
print("the perimeter is", Rectangle2.get_perimeter)
print("the area is", Rectangle2.get_area)

print("the result")