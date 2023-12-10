import random

random_number = random.randint(1, 13) #Create a first variable for the randon number
random_number_2 = random.randint(1, 13) #Create the second variable that is going to be guess number
    #random.randint to define a min and max number that can be chosen

print(f"The first number is:", random_number) #Print the first randon number  
print("\n")


while True:
    guess1 = input("write 'higher' or 'lower' to indicate what the next card will be: ") #Create a first input that will be only "higher" or "lower"

    if guess1 == "higher": #if "higher", then it'll compare the 2 randon numbers and see if it is correct the comparison between the randon's
        if random_number < random_number_2:
            print ("\nYou are correct!")
            break
        elif random_number > random_number_2:
            print("\nYou are wrong.")
            break
        else:
            print("\nThe numbers are equal, sorry.")
            break

    elif guess1 == "lower": 
        if random_number < random_number_2: #See if the first number is lower then the second secret number 
            print ("\nYou are wrong.")
            break
        elif random_number > random_number_2:
            print("\nYou are correct!")
            break
        else:
            print("\nThe numbers are equal, sorry.")
            break
            
            #For each finding, the loop will be broken 


    elif guess1 != "lower" or "higher": # if the input is neither "lower or higher", it'll print and go back to the beginning
        print("Write only 'lower' or 'higher' ")
        print("\n")
        


print("\n")


print(f"The first number is:", random_number)
print(f"The second number is:",random_number_2)










"""if random_number == 1:
    print("Ace")

elif 2 <= random_number <= 10:
    print(random_number)

elif random_number == 11:
    print("Jack")

elif random_number == 12:
    print("Queen")

elif random_number == 13:
    print("King")"""