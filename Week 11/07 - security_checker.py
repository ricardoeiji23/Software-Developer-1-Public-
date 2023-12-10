rate_list = ["Rate 1", "Rate 2", "Rate 3", "Rate 4", "Rate 5"]

votes_dictionary = {rates: {"quantity": 0, "total_rating": 0} for rates in rate_list}

total_votes_all_rates = 0

while True:
    user_input = input("Enter a rating (1-5) or -1 to end: ")

    if user_input == "-1":
        break

    try:
        user_input = int(user_input)

        if 1 <= user_input <= len(rate_list):
            selected_rate = rate_list[user_input - 1]
            votes_dictionary[selected_rate]["quantity"] += 1
            votes_dictionary[selected_rate]["total_rating"] += user_input
            total_votes_all_rates += 1

        else:
            print("Please, choose a number from 1 - 5")

    except ValueError:
        print("Please, enter a valid rate (1-5) or -1 to end")

for rate, data in votes_dictionary.items():
    quantity = data["quantity"]
    total_rating = data["total_rating"]
    
    if quantity > 0:
        average_rating = total_rating / quantity
        print(f"{rate} quantity: {quantity}, Average Rating: {average_rating:.2f}")
    else:
        print(f"{rate} quantity: {quantity}, No votes recorded.")
