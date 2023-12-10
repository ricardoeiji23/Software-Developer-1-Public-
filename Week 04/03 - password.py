password = str("Rocket") #Set the password

while True: #Infinite loop
    
    input_user = str(input("\nEnter the password: ")) #Ask for a user input (String)
    
    if input_user.lower() == password.lower(): #transforming the input to lower #see if the input is equal to the password in lower 
        print("\nAccess confirmed. Welcome!") #if true, print and break the loop
        break
    else:
        print("\nInvalid password") #Else, print invalid and continue the loop