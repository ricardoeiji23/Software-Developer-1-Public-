print("PEACHERS")
peaches_many = int(input("How many peaches? "))
peaches_price = float(input("Price per peach? "))

print("\nBEANS")
beans_many = int(input("How many beans? "))
beans_price = float(input("Price per beans? "))

print("\nCHICKEN PIECES")
chicken_many = int(input("How many Chicken pieces? "))
chicken_price = float(input("Price per Chicken pieces? "))

print("\nSOCKS")
socks_many = int(input("How many socks? "))
socks_price = float(input("Price per sock? "))

print("\nBOTTLE OF WATER")
water_many = int(input("How many bottle of water? "))
water_price = float(input("Price per bottle of water? "))

total_items_purchased = (peaches_many + beans_many + chicken_many + socks_many + water_many)

weekly_shop = ((peaches_many*peaches_price) + (beans_many*beans_price) + (chicken_many*chicken_price) + (socks_many*socks_price) + (water_many*water_price))

print("\nThe total number of items purchased is:", str(total_items_purchased))
print("\Your weekly shop cost is:", str(weekly_shop))