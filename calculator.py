#!/usr/bin/env python3
# Created By: Ferdous Sediqi
# Date: May, 10, 2022
# This program asks the user for 2 numbers then calculate
# numbers using calculator function with 3 different parameters.


# function for calculation
def calculator(operation, num_1, num_2):
    # if statements for doing different math oprations
    if operation == "+":
        total = num_1 + num_2
        return total
    elif operation == "-":
        total = num_1 - num_2
        return total
    elif operation == "*":
        total = num_1 * num_2
        return total
    elif operation == "/":
        total = num_1 / num_2
        return total
    else:
        print("Your operator input was not valid.")
        

def main():

    try:
        # Get user inputs and convert it to float

        sign = input("Enter your prefer Math operation (+, -, *, /): ")
        first_num_string = input("Enter your first number: ")
        second_num_string = input("Enter your second number: ")
        first_num_float = float(first_num_string)
        second_num_float = float(second_num_string)
        print("")

     
        calc = calculator(sign, first_num_float, second_num_float)
        print("The result of ", first_num_float, sign, second_num_float, "is {:.2f}". format(calc))


    # invalid input
    except Exception:
        print("")
        print("Invalid input. Input was not a number.")


if __name__ == "__main__":
    main()
