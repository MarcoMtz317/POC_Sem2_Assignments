number1 = 0
number2 = 0
try:
    number1 = int(input("enter a number"))
    number2 = int(input("enter a number"))
except ValueError:
    print("integer wasn't given")
    

try:
    answer = number1/number2


except ZeroDivisionError:
    print("divide by 0 is not possible")
    