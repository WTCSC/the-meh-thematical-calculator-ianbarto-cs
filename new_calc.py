# This is the main calculation file that takes the input calculations and outputs the answer, as well as the numbers and the calculations that they have inputted
from time import sleep

# Defines the calculations needed to run the calculator

def add(a, b):
    return a + b
# Add adds the two values inputted ex: 4 + 3 = 7
def subtract(a, b):
    return a - b
# Subtracts the two values inputted ex: 4 - 2 = 2
def multiply(a, b):
    return a * b
# Multiplies the two values inputted ex: 4 x 3 = 12
def divide(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Division by zero is not allowed.")
#Checks to make sure that you are not dividing by zero, because that it breaking the rules of zero, then divides like so ex: 12 / 3 = 4
def exponent(a, b):
    return a ** b
    
#Gets the numbers and the operation that is requested, for use in the main() function

def number1():
    return float(input("Enter first number: "))
def number2():
    return float(input("Enter second number: "))
def operation():
    return input("Enter operation (+, -, *, /, ^): ")
def again():
    calc_again = input("Do you want to calculate again? (y/n): ")
    if calc_again.lower() == "y":
        return True
    else:
        print("Exiting the calculator. Goodbye!")
        return False

#The main function that gets both the calculations, and then runs the calculation functions, returning the values


def main():    
    while True:
        a = number1()
        b = number2()
        operation = operation()
        if operation == '+':
            print(f"{a} + {b} = ", int(add(a, b)))
            sleep(1)
            if not again():
                break
        elif operation == '-':
            print(f"{a} - {b} = ", int(subtract(a, b)))
            sleep(1)
            if not again():
                break
        elif operation == '*':        
            print(f"{a} * {b} = ", int(multiply(a, b)))
            sleep(1)
            if not again():
                break
        elif operation == '/':
            try:
                print(f"{a} / {b} = ", int(divide(a, b)))
            except ValueError as e:
                print(e)
            sleep(1)
            if not again():
                break
        elif operation == '^':
            print(f"{a} ^ {b} = ", int(exponent(a, b)))
            sleep(1)
            if not again():
                break

# This is put in place in order to prevent this file from running when you run pytest
if __name__ == "__main__":
    main()