rainbow_list = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo","Violet"] #list with all the colors 

while True: #Infinit loop
    try: #Try to see if it's going to be a integer number
        user_input = int(input("Enter a number between 1 and 7 (-number to end): ")) #Ask the user for a number between 1-7 or a negative number to quit the program

        if user_input < 0: #If the input is negative, break and end the program
            print("Program terminated")
            break
            
        elif 1 <= user_input <=7: # If the input is between 1 and 7
            color_index = user_input-1 # O index começa com 0, então precisa diminuir 1 no input (input 5 = index 4[Começa com 0] - Precisa diminuir 1 no input para igualar no index)

            color = rainbow_list[color_index] # Create a variable to store the color from the list with the index

            print(f"The corresponding color is: {color}\n") # Print the new variable (That is the list with the index) 

        else:
            print("Invalid input, please chose between 1 and 7 (Or a negative to end)\n")

    except ValueError:
        print("Plase, input a integer number\n")
