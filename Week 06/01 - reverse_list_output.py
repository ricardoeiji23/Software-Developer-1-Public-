# Create a list to store the integers
integers = []

# Prompt the user for 5 integers
for i in range(5):
    try:
        num = int(input(f"Enter integer {i + 1}: "))
        integers.append(num)
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Print the inputted integers in reverse order
print("\nReversed Integers:")
for i in range(len(integers) - 1, -1, -1): 
        # The "i" is reading the "integers" in a reversed order
        # len(integers) - 1 -> Starts from the last index
        # -1 -> It goes down to the -1
        # -1 -> With a step of -1  
    print(integers[i])
        # Will print the numbers that started from the end to the begin
