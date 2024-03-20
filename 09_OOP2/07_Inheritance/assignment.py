class Rectangle:
<<<<<<< HEAD

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
 
    def __str__(self) -> str:
        return "Rectangle of base:" + self.__base + ", height:" + self.__height


 
rectangle1 = Rectangle(3, 4)
print("the base is " , rectangle1.get_base)
print("the height is", rectangle1.get_height)
print("the perimeter is", rectangle1.get_perimeter)
print("the area is", rectangle1.get_area)
print("area")
Rectangle2 = Rectangle(4, 3)
print("the base is " , Rectangle2.get_base)
print("the height is", Rectangle2.get_height)
print("the perimeter is", Rectangle2.get_perimeter)
print("the area is", Rectangle2.get_area)
print("area")

class square(Rectangle):
    def __init__(self, side_length:float) -> None:
        super().__init__(side_length, side_length)
        self.__side_length = side_length

    def get_side_length(self) -> float:
        return self.__side_length

    def __str__(self) -> str:
        return "square with side length:" + str(self.__side_length)

square1 = square(3)
print(square1)
print("the base of square1 is", square1.get_base())
print("the height of square1 is", square1.get_height())
print("the side length of square1 is", square1.get_side_length())
print("the area of square1 is", square1.get_area())
print("the perimeter of square1 is", square1.get_perimeter())
=======
    def __init__(self, base: float, height: float) -> None:
        if (base < 0):
            self.__base = 0
        else:
            self.__base = base

        if (height < 0):
            self.__height = 0
        else:
            self.__height = height

    def get_height(self) -> float:
        return self.__height

    def get_base(self) -> float:
        return self.__base

    def get_perimeter(self) -> float:
        return 2 * self.__base + 2 * self.__height

    def get_area(self) -> float:
        return self.__base * self.__height

    def __str__(self) -> str:
        # Rectangle with base:3, height:4
        return "Rectangle with base:" + str(self.__base) + ", height:" + str(self.__height)
    
class Square(Rectangle):
    def __init__(self, side: float) -> None:
        super().__init__(side, side)
        self.__side = side
        
    def get_side(self) -> float:
        return self.__side
    
    def __str__(self) -> str:
        # Square with side:3
        return "Square with side:" + str(self.__side)
    
square1 = Square(3)
print(square1)
print("The side of square1 is", square1.get_side())
print("The perimeter of square1 is", square1.get_perimeter())
print("The area of square1 is", square1.get_area())
print()
rectangle1 = Rectangle(3, 4)
print(rectangle1)
print("The base of rectangle1 is", square1.get_base())
print("The height of rectangle1 is", square1.get_height())
print("The perimeter of squarectangle1re1 is", square1.get_perimeter())
print("The area of rectangle1 is", square1.get_area())
>>>>>>> 4bb0de8b3b7ea165df514680e62fe3e5a4314d2a
