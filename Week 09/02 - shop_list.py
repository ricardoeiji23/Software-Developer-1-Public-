shop_list = [] #Create the list for storing the inputs

for i in range(5): #Create a range in which the limit will be when i hit 5
    item_name = input(f"Enter the name of the item {i + 1}: ") #Variable for the name (here will be incremented the number to the "i")
    price_item = float(input(f"Enter the price of the {item_name}: $")) #Ask for the value of the item

    shop_list.append((item_name, price_item)) #Precisa deixar todas as variáveis dentrod de único () porque só podemos adicionar 1 valor na list


shop_list.sort(key=lambda x: x[1], reverse=True) # Sorting the values in the list - "(key=lambda x: x[1], reverse=True)" -Code for sorting by the number of the values
    #key=lambda x: x[1] -> This code is extracting the second value (1, since 0 is the first) of the list to be the base of the sorting
    #reverse=True -> When set to "True", it will be in descending order (False is ascending order)

print("\nThe sorted shop list is: ")

for x, y in shop_list:
    print(f"{x}: ${y:.2f}") #limiting the decimanal numbers -> ":.2f" code for limiting to 2