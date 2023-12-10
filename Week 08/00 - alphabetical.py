user_string = []

for i in range(5):
    user_input = input(f"Enter 5 strings {i + 1}:") #Will be adding in "i" until it reaches 5
    user_string.append(user_input) # Add the users input in the string list 
    
user_string.sort() #The .sort() is used to sort alphabetically

print("Sorted strings: ")
for string in user_string:
    print(string) #Basically printing each string in the list