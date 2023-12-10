"""
Inputs
    total in party
    number of adults
    number of concessions (Over 65 years old)

Price
    Adult - 10.50
    Child - 7.30
    Concessions - 8.40

Auto offers
    For 10 kids - 1 free adult  
    10% if the bill is over 100.00

Ps
    1 kid - at least 1 adult
    Tickets collected in person? No additional charge 
    postage & packaging, which costs £2.34, is added after all offers have been applied 

"""

print("For the ticket requirements:\n")

number_total_InParty = int(input("Enter the number of total people in the party: "))
number_adults = int(input("Enter the number of adults: "))
number_of_concessions=int(input("Enter the number of concessions: "))

numberOfKids = number_total_InParty - (number_adults+number_of_concessions) #Finding the number of the kids (The rest)

total_price_kids = float(numberOfKids * 7.30) #Calculate the cost for the kids

number_free_tickets_adults = numberOfKids // 10 # Adultos de graça = número de crianças 

cost_free_tickets_adults = float(number_free_tickets_adults*10.50) #Calculate the total price of the free tickets of adults

total_price_adults = float((number_adults*10.50) - cost_free_tickets_adults) #Calculate the total price for the adults (No free)

total_price_concessions = float(number_of_concessions*8.40) #Calculate the price of concessions

total_bill = float(total_price_adults+total_price_concessions+total_price_kids) #Calculate the total bill

total_bill_w_discount = float(total_bill-(total_bill*0.10)) #Calculate the bill with the discount

print(
    "\n\nInformation about your purchase:"
    f"\nNumber of kids: {numberOfKids}"
    f"\nCost of kids: {round(total_price_kids, 2)}"

    f"\n\nNumber of adults: {number_adults}"
    f"\nCost of adults: {round(total_price_adults,2)}"

    f"\n\nNumber of concessions: {number_of_concessions}"
    f"\nCost of concessions: {round(total_price_concessions, 2)}"

    f"\n"

    f"\nThe total price of the bill: {round(total_bill_w_discount, 2)}"
)