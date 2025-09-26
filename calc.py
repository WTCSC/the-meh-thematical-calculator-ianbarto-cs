from time import sleep

def add():
    print(f"{number1} + {number2} = ",int(number1 + number2))
def subtract():
    print(f"{number1} - {number2} = ",int(number1 - number2))
def multiply():
    print(f"{number1} * {number2} = ",int(number1 * number2))
def divide():
    if number2 != 0:
        print(f"{number1} / {number2} = ",int(number1 / number2))
    else:
        print("Are you trying to break the calculator? Division by zero is not allowed, you dingus mofo.")
def exponent():
    print(f"{number1} ^ {number2} = ",int(number1 ** number2))

def again():
    calc_again = input("Do you want to calculate again? (y/n): ")
    if calc_again.lower() == "y":
        return True
    else:
        print("Exiting the calculator. Goodbye!")
        return False

while True:
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /, ^): ")
    
    print("Calculating...")
    sleep(1)
    print("Still calculating...")
    sleep(1)
    print("Almost there...")
    sleep(1)

    if operation == '+':
        add()
        sleep(1)
        if not again():
            break
    elif operation == '-':
        subtract()
        sleep(1)
        if not again():
            break
    elif operation == '*':
        multiply()
        sleep(1)
        if not again():
            break
    elif operation == '/':
        divide()
        sleep(1)
        if not again():
            break
    elif operation == '^':
        exponent()
        sleep(1)
        if not again():
            break
    else:
        print("Invalid operation you dingus typer, try again and don't break the calculator")

