import random

# Function to initialize the game grid
def initialize_grid():
    cards = ['Jack', 'Queen', 'King', 'Ace']
    deck = cards * 4
    random.shuffle(deck)
    grid = [['*' for _ in range(4)] for _ in range(4)]
    return grid, deck

# Function to display the game grid
def display_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()

# Function to check if the game is completed
def is_game_complete(grid):
    for row in grid:
        if '*' in row:
            return False
    return True

# Main game loop
def play_game():
    grid, deck = initialize_grid()
    selections = 0

    while not is_game_complete(grid):
        display_grid(grid)

        # Prompt the user for the first card position
        try:
            row1 = int(input("Enter row for the first card: "))
            col1 = int(input("Enter column for the first card: "))
            card1 = grid[row1][col1]
            print(f"Card at {row1} {col1}: {card1}")

            # Check if the card has already been paired
            if card1 == 'X':
                print("This card has already been paired. Try again.")
                continue

            # Prompt the user for the second card position
            row2 = int(input("Enter row for the second card: "))
            col2 = int(input("Enter column for the second card: "))
            card2 = grid[row2][col2]
            print(f"Card at {row2} {col2}: {card2}")

            # Check if the second card has already been paired
            if card2 == 'X':
                print("This card has already been paired. Try again.")
                continue

            # Check if the cards match
            if card1 == card2:
                print("Matching pair! Well done.")
                grid[row1][col1] = 'X'
                grid[row2][col2] = 'X'
            else:
                print("Not a matching pair. Try again.")

            selections += 1

        except (ValueError, IndexError):
            print("Invalid input. Please enter valid row and column numbers.")

    print(f"\nGame completed! Total number of selections: {selections}")

# Play the game
play_game()
