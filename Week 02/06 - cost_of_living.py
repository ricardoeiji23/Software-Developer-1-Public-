rent = float(input("Rent per month: "))
gas = float(input("Gas Payment per month: "))
electricity = float(input("Electricity payment per month: "))
water = float(input("Water payment per month: "))
council_tax = float(input("Concil tax payment per month: "))

total = rent+gas+electricity+water+council_tax

print("\n")

print("Your monthly expenses are:")
print("Rent:               ", "$ ", rent)
print("Gas:                ", "$ ", gas)
print("Electricity:        ", "$ ", electricity)
print("Water:              ", "$ ", water)
print("Concil tax:         ", "$ ", council_tax)

print("\n")

print("-------------------------------------")

print("Total:              ", "$ ", round(total, 2))

print("-------------------------------------")

