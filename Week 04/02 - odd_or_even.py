while True: #Creating a infinite loop (Use break to get out of the program)
    try: #If the user input anything else a integer, it's going to the "except ValueError"
        user_input = int(input("\nEnter a positive integer: ")) #Ask for a input

        is_even = (user_input % 2 == 0) #Create a variable that is going to be a boolean variable

        if is_even: #If the variable is TRUE, it's even
            print(f"\n{user_input} is an even number.")
        else:
            print(f"\n{user_input} is an odd number.")
            
        continue_or_not = input("\nDo you want to continue? (Y/N): ").lower() 
            #Create a variable_input in which the user will write "y" or any other character
            #To transform the input into lower, we can use ".lower()" beside the input
        
        if continue_or_not != 'y': #If the variable is different to "y", then it means that it's exiting 
            print("Exiting program.")
            break #break the white true loop
            
    except ValueError: 
        print("\nEnter a positive integer number!")
        
