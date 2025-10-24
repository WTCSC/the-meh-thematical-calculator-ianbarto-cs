from time import sleep

def add(number1, number2):
    print(f"{number1} + {number2} = ",int(number1 + number2))
def subtract(number1, number2):
    print(f"{number1} - {number2} = ",int(number1 - number2))
def multiply(number1, number2):
    print(f"{number1} * {number2} = ",int(number1 * number2))
def divide(number1, number2):
    if number2 != 0:
        print(f"{number1} / {number2} = ",int(number1 / number2))
    else:
        print("Are you trying to break the calculator? Division by zero is not allowed, you dingus mofo.")
def exponent(number1, number2):
    print(f"{number1} ^ {number2} = ",int(number1 ** number2))

def again():
    calc_again = input("Do you want to calculate again? (y/n): ")
    if calc_again.lower() == "y":
        return True
    else:
        print("Exiting the calculator. Goodbye!")
        return False

def main():
    while True:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /, ^): ")
        a = number1
        b = number2
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

if __name__ == "__main__":
    main()