"""
- Ask for a positive number that represents the minutes 
- Calculate the basic call charge (Minutes * Call rate)
- Calculate the VAT (Basic call charge * VAT rate)
- Calculate the total bill (Basica call + VAT)

- Print all the requirements requested
"""

minutes=int(input("Enter a positive number of minutes: "))
print("\n")

print("Number of minutes used:", str(minutes), "\n")

call_rate = 0.15 # 15 perce per minute 
vat_rate = 0.20 # 20% 

basic_call_charge = minutes*call_rate 

vat = basic_call_charge*vat_rate

total_bill = basic_call_charge + vat
total_bill_round = round(total_bill, 2)
    #Código para limitar o decimal em 2 números

print("Basic call charge: $", str(basic_call_charge),"\n")
print("VAT due: $", str(vat),"\n")
print("Total bill: $", str(total_bill_round),"\n")

