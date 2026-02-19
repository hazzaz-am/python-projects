
items: list[str] = []
prices: list[int | float] = []
total = 0

while True:
  item = input("Enter your item or Press q to Quit: ")
  if item.lower() == "q":
    break
  else:
    price = float(input(f"Enter the price of {item}: $"))
    items.append(item)
    prices.append(price)
  

print("\n\n\n----- YOUR CART -----\n\n\n")

for i in range(len(items)):
  print(f"{items[i].capitalize()} ----- ${prices[i]}")

print("------------------")

for i in prices:
  total += i

print(f"Total: ------ {total}")

