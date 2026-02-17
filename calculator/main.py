"""
Take an Operator, Two Numbers and perform an Operation based on the Operator
"""

operator = input("Enter an Operator (+ - * /): ")
number1 = float(input("Enter the 1st number: "))
number2 = float(input("Enter the 2nd number: "))

if operator == "+":
  result = number1 + number2
  print(round(result, 3))
elif operator == "-":
  result = number1 - number2
  print(round(result, 3))
elif operator == "*":
  result = number1 * number2
  print(round(result, 3))
elif operator == "/":
  result = number1 / number2
  print(round(result, 3))
else:
  print(f"{operator} is not a Valid Operator")
