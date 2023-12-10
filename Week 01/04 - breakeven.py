#Break-even = total revenue equals the business expenses(Fixed costs) 

# Cost to produce each item
# Sale price per item (Item cost + profit per item)
# Fixed costs 

# Breakeven is the fixed costs / (sale price - item cost)
    # So vai ter um breakeven quando o lucro retirando o custo do produto bater com o custo fixo

cost_to_produce_each_item = 20.00
sale_price_per_item = 40.00
fixed_costs = 50000.00

breakeven = fixed_costs/(sale_price_per_item-cost_to_produce_each_item)

print("The cost to produce each item is:", str(cost_to_produce_each_item),"\n")
print("The sale price per item is:", str(sale_price_per_item),"\n")
print("The fixed cost is:", str(fixed_costs),"\n")

print("The breakeven is:", str(breakeven), "items")
