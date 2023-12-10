def reverse_function(num):
    return int(str(num)[::-1]) 
        # First we are transforming the "num" in a string to invert with "[::-1]"
        # Then we transform the inverted string into a integer number 

while True:        
    
    try:
        user_input = input("Enter a positive number that have between 2 to 10 digits or a negative number to exit: ") # Ask for the input according with the criterias 
        num=int(user_input) # Defining the "num" with the input of the user 
        string_num = str(num) # Transforming the "num" into a string and defining it in a variable 
        
        if 2 <= len(string_num) <= 10: # To use the "len" it has to ba a string # Defining the size of the string and the limitations 
            if num < 0: 
                print("Exiting the program")
                break # We putted this first because it's only going to happen if activate the "if" otherwise it'll go to the next block 
            
            reversed_num = reverse_function(num) # Defining the variable for the function
            print(f"The reversed integer: {reversed_num}") # Print the result of the number inversed 

        else:
            print("Enter a valid number!") # It's going to activate if it not between 2 - 11

    except ValueError:
        print("Please enter a valid integer number!") # It's going to activate if it not a integer positive number 
