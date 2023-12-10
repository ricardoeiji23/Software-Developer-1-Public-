def reverse_string(input_str):
    if len(input_str) <= 1: #If have only 1 caracter
        return input_str #Return this only caracter
    
    else:
        return reverse_string(input_str[1:]) + input_str[0]
            # "input_str[1:]" - Extracts a substring starting with the index 1 to the end of the string
                # It takes the "icardo" of ricardo 

def main():
    user_input = input("Enter a string: ")
    reversed_string = reverse_string(user_input)

    print(f"The reverser string: {reversed_string}")


main()