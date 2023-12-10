rates_in_dictionary = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
total_votes_from_all = 0

while True:
    try:
        user_input = input("Enter a rating (1-5) or -1 to end: ")

        if user_input == "-1":
            break

        user_input = int(user_input)

        if 1 <= user_input <= 5:
            rates_in_dictionary[user_input] += 1 #Adding the increment for the specific key in the dictionary 
            total_votes_from_all += 1 

        else:
            print("Invalid rating. Please enter a number between 1 and 5.")

    except Exception as ve:
        print(f"Error: {ve}. Please enter a valid number.")

# Output the table
print("\nRating\tCount\tAverage")
print("----------------")
for i in range(1, 6): 
    number_of_votes = rates_in_dictionary[i] # "rates_in_dictionary[i]" represents the value of the key

    average_rating = number_of_votes / total_votes_from_all
    average_rating_percentage = average_rating * 100
    rounded_average_rating_percentage = round(average_rating_percentage, 2)

    print(f"{i}\t{number_of_votes}\t{rounded_average_rating_percentage}")
        #It's creating a range from 1-6 and the "i" will run each item in the dictionary