"""
- User will have to input from 1-5 
- End the program with -1
- After all votes, it will show how many people gave each rating and the average rating.
    Avarage = total votes / 

- Use the exceptions and output warning 
"""

rate_list = ["Rate 1", "Rate 2", "Rate 3", "Rate 4", "Rate 5"]

votes_dictionary = {rates:0 for rates in rate_list}

total_votes_all_rates = 0



while True:

    user_input = input("Enter a rating (1-5) or -1 to end: ")

    if user_input == "-1":
        break

    try:
        user_input = int(user_input)

        if 1 <= user_input <= len(rate_list):
            selected_rate = rate_list[user_input - 1]
            votes_dictionary[selected_rate] += 1 #Adding +1 in the dictionary that is related to the list index (A string is co-related to a number)

            total_votes_all_rates += 1

        else:
            print("Please, choose a number from 1 - 5")

    except ValueError:
        print("Please, enter a valid rate (1-5) or -1 to end")

for x, y in votes_dictionary.items():
    average = int(y) / total_votes_all_rates
    average_percentage = average * 100
    
    print("\nRate Number\tQuantity of votes\tAverage")
    print(f"{x}\t\t{y}\t\t\t{round(average_percentage, 2)}%")
