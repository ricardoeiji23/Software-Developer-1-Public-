import random #import the randon

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (Rock, Paper, or Scissors): ").strip().capitalize() #Remove the space #capitalize all letters
        if user_choice in ["Rock", "Paper", "Scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

user_score = 0
computer_score = 0

while user_score < 3 and computer_score < 3: # While none achive 3, the program will continue running
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose {user_choice}. Computer chose {computer_choice}.")

    if user_choice == computer_choice: #If the options are equal, it's a tie
        print("It's a tie!\n")

    elif ( #To add more than one situation, use the () and the "and, or" #Adding all the options that the user wins
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Scissors" and computer_choice == "Paper") or
        (user_choice == "Paper" and computer_choice == "Rock")
    ):
    
        print("You win this round!\n")
        user_score += 1

    else: # The else if going to the rest, which it when the computer wins (Add all the options and then use the else)
        print("Computer wins this round!\n")
        computer_score += 1

print("\nGame over!\n")

if user_score > computer_score:
    print("You win the game!\n")
elif computer_score > user_score:
    print("Computer wins the game!\n")
else:
    print("It's a tie!\n")

print(f"Your score: {user_score}")
print(f"Computer's score: {computer_score}")
