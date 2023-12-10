import random

def get_user_input():
    while True:
        user_input = input("Enter (Rock, Paper or Scissors): ").strip().capitalize()
        if user_input in ["Paper", "Rock", "Scissors"]:
            return user_input
        else:
            print("Please, Enter (Rock, Paper or Scissors!)")


def get_computer_input():
    return random.choice(["Paper", "Rock", "Scissors"])


score_computer = 0
score_user = 0

while score_computer < 3 and score_user < 3:
    user_input = get_user_input()
    computer_input = get_computer_input()

    print(f"Your choice: {user_input}")
    print(f"Computer's choice: {computer_input}")

    if computer_input == user_input:
        print("It was a draw")
    elif (
        (user_input=="Paper" and computer_input=="Rock") or
        (user_input=="Rock" and computer_input=="Scissors") or
        (user_input=="Scissors" and computer_input=="Paper")
    ):
        print("Congratulations, you win!")
        score_user += 1
        print(f"You need: {3-score_user} to complete the game")
        print("***************************")
    else:
        print("The computer won.")
        score_computer += 1
        print(f"Computer needs: {3-score_computer} to complete the game")
        print("***************************")

print("Game is over!")

if score_computer > score_user:
    print("Final decision: Computer won!")
else:
    print("Final decision: You won!")

print("\n")

print(f"Your score:{score_user}")
print(f"Computer's score:{score_computer}")



        