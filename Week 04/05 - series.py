num1 = int(input("Enter a positive or negative number for the first number: "))
num2 = int(input("Enter a positive or negative number for the second number: "))
num3 = int(input("Enter a positive or negative number for the third number: "))
num4 = int(input("Enter a positive or negative number for the fourth number: "))
num5 = int(input("Enter a positive or negative number for the fifth number: "))
    #Ask for 5 variable_inputs of a positive or negative number

print("\n")

positive_sum=0
negative_num=0
    #Define the variable to storage the positive and negative numbers

if num1 >= 0: #If the first number is grater then 0 is positive
    positive_sum+=num1 #if positive, it'll be added into the positve number storage
else:
    negative_num+=num1 #else, it's negative and it's storage in the negative storage

if num2 >= 0:
    positive_sum+=num2
else:
    negative_num+=num2

if num3 >= 0:
    positive_sum+=num3
else:
    negative_num+=num3

if num4 >= 0:
    positive_sum+=num4
else:
    negative_num+=num4

if num5 >= 0:
    positive_sum+=num5
else:
    negative_num+=num5


print(f"Sum up of positive numbers: {positive_sum}") 
print(f"Sum up of negative numbers: {negative_num}")
    #Print the storage of positive and negative numbers 