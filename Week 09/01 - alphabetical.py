#Create an empty list to store the strings 
list_of_strings = []


while True:
    # Loop to take 5 strings from the user
    for i in range(5):
            user_input = input(str((f"Enter string {i+1}: ")))
            list_of_strings.append(user_input) #Add the inputs in the list 

    #This code will sort the list of strings
    list_of_strings.sort()

    #The title of the prompt
    print("\nSorted strings:")

    #Code for showing each item of the list
    for string in list_of_strings:
        print(string)
    
    
    break # It can't be indented or it'll cut in the first loop
        
    