try:
    value1 = int(input('Enter an integer: '))
    value2 = int(input('Enter an integer:'))
    print('The inverse of', value1, 'is', 1/value2)
except ValueError:
    print('You did not provide a number, so I will not calculate the inverse')
except ZeroDivisionError:
    print('You provided 0 and division by 0 is not possible, sorry')
except:
    print('Something strange happened here, sorry')