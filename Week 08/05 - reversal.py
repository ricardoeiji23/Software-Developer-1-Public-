
# With slicing 
string_input = input("Enter a string: ")

reversed_string = string_input[::-1]

print(reversed_string)

#With list
string_input2 = input("Enter a string (Can be 2 or +): ")

reversed_string2 = ''.join(list(reversed(string_input2)))

print(reversed_string2)
