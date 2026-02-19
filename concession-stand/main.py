menu: dict[str, int | float] = {
  "pizza": 3.00,
  "nachos": 4.50,
  "popcorn": 6.00,
  "fries": 2.50,
  "chips": 1.00,
  "pretzel": 3.50,
  "soda": 3.00,
  "lemonade": 4.25,
}

cart: list[str] = []
total = 0

print("-------------- MENU --------------")
for key, value in menu.items():
  item = key.capitalize()
  print(f"{item:10}: ${value:.2f}")
print("-------------- MENU --------------")

while True:
  food = input("Select an item (q to quit): ")

  if food.lower() == "q":
    break
  elif menu.get(food) is not None:
    cart.append(food)

for food in cart:
  total += menu[food]

print()
print(f"Total is: ${total:.2f}")