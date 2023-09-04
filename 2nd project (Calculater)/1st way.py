'''
Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.
Perform the calculation and display the result.
'''

# ///////////////////////////////////////////////////////////////////////////////////////////////////////


operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 5))

elif operator == "-":
    result = num1 - num2
    print(round(result, 5))

elif operator == "*":
    result = num1 * num2
    print(round(result, 5))

elif operator == "/":
    result = num1 / num2
    print(round(result, 5))

else:
    print(f"{operator } is not a valid operater")