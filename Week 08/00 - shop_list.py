items_and_prices = []

for i in range(5):
    item_name = input(f"\nEnter the item {i + 1} name: ")
    item_price = float(input(f"Enter the price of the {item_name}: $"))
    items_and_prices.append((item_name, item_price))
    
    
items_and_prices.sort(key=lambda x: x[1], reverse=True)

print("\nSorted items by price (Highest to lowest):")

for x, y in items_and_prices:
    print(f"{x}: ${y:.2f}")