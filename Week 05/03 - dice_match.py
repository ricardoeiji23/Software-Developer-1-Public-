import random 

def roll_dice():
    return random.randint(1, 6)


def main():
    dice1 = roll_dice()
    dice2 = roll_dice()
    throws = 1

    print(f"Throw{throws}: Dice 1: {dice1}, Dice 2: {dice2}")

    while dice1!=dice2:
        dice1 = roll_dice()
        dice2 = roll_dice()
        throws += 1

        print(f"Throw{throws}: Dice 1: {dice1}, Dice 2: {dice2}")
    
    print(f"After {throws} throws, the dices matched!")


main()
