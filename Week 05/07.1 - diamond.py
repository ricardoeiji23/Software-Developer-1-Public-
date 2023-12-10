def print_diamond(width):
    if width < 2 or width > 40:
        print("Please enter a width between 2 and 40.")
        return

    for i in range(1, width, 2):
        print(" " * ((width - i) // 2) + "*" * i)
    
    for i in range(width, 0, -2):
        print(" " * ((width - i) // 2) + "*" * i)

while True:
    user_input = input("Enter the width of the diamond (2 to 40): ")

    try:
        width = int(user_input)
        print_diamond(width)
    except ValueError:
        print("Please enter a valid integer.")
