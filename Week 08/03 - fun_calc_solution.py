"""
- Created a function for each operation
- Created a fucntion for the calculator (Which takes 3 parameters... The number of the operation, num1, num2) (In this function it prints the result already)
- Creates the main function (Ask for the 2 numbers) (The operators number) (Call the function "Calculator" with the 3 parameters)

- Call main function
"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("Error: Cannot divide by zero.")
        return None

def remainder(x, y):
    if y != 0: #different
        return x % y #Will give the remainder of the division 
    else:
        print("Error: Cannot calculate remainder when divisor is zero.")
        return None

def calculator(choice, x, y): #Takes 3 parameters #They represent the "(choice, num1, num2)" of the user's input

    operations = { #Dictionary and the values of the keys are related directly to the functions
        1: add, #Seperate with a "," the values of the keys
        2: subtract,
        3: multiply,
        4: divide,
        5: remainder
    }

    if choice in operations: # Check if the choice(key) is present in the dictionary
        result = operations[choice](x, y) # The result of the functions calculation will be stored in "result" # Dictionary[Key] (Values of the function)
        if result is not None: #If the result isn't empty, print the result
            print(f"The result is: {result}")
    else:
        print("Invalid choice. Please select a number between 1 and 5.")

def main(): # Main function that will firstly run in the program
    try:
        # Prompt the user to enter two integers
        num1 = int(input("Enter the first integer: "))
        num2 = int(input("Enter the second integer: "))

        # Display the menu
        print("\nMenu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Remainder\n")

        # Get the user's choice for the operation
        choice = int(input("\nSelect an operation (1-5): "))

        # Perform the selected operation
        calculator(choice, num1, num2) #Call the function and added the parameters (choice, num1, num2)

    except ValueError: #will display if the first input is not integer value
        print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()
