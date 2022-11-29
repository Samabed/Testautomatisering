# Program make a simple calculator that can add, subtract, multiply and divide using functions

import argparse


class Calculator:
    def __init__(self):
        pass

    # define functions
    def add(self, x, y):
        """This function adds two numbers"""

        return x + y

    def subtract(self, x, y):
        """This function subtracts two numbers"""

        return x - y

    def multiply(self, x, y):
        """This function multiplies two numbers"""

        return x * y

    def divide(self, x, y):
        """This function divides two numbers"""

        return x / y


my_parser = argparse.ArgumentParser()
my_parser.add_argument('--manual', action='store_true', default=False)

args = my_parser.parse_args()
if args.manual:

    # take input from the user
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    choice = input("Enter choice(1/2/3/4):")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", Calculator().add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", Calculator().subtract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", Calculator().multiply(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", Calculator().divide(num1, num2))
    else:
        print("Invalid input")
