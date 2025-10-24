from time import sleep

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Division by zero is not allowed.")
def exponent(a, b):
    return a ** b
    
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
if __name__ == "__main__":
    main()