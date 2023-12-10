sum_positive = 0 #Create the variable to store the sum 
sum_negative = 0


for i in range(10): #Defined the loop times with the limit when i=10 (10 integer values)
    try: # Used to handle if it's not a integer input 
        num = int(input(f"Enter a positive or negative number{i + 1}: ")) # After inputing a number the "i" in range will be add 1 number (That's the countdown)
        if num > 0: # If the number is greater than 0 (positive) add this number in the variable 
            sum_positive += num 
        elif num < 0: # If the number is lower than 0 (negative) add this number in the variable
            sum_negative += abs(num) #sum = sum + num(input) 
    
    except ValueError: # If it's not a integer, it'll genenate this code 
        print("Invalid input. Please enter a integer number.")
        

print(f"Sum of positive numbers: {sum_positive}")
print(f"Sum of negative numbers: {sum_negative}")


