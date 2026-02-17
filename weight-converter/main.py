"""
Take Weight and Unit from User and convert Weight based on the Unit.
"""

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds ? (K OR L): ")

if unit == "K" or unit == "k":
  weight = round(weight * 2.205, 1)
  unit = "Lbs."
  print(f"Your weight is {weight} {unit}")
elif unit == "L" or unit == "l":
  weight = round(weight / 2.205, 1)
  unit = "Kgs."
  print(f"Your weight is {weight} {unit}")
else:
  print(f"{unit} is not Valid Unit.")

