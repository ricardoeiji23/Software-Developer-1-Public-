"""
- Take the task 1 
- Add: Calculates and outputs the average of the positive and the average of the negative integers entered 
- Appropriate messages should be output if there were no positive numbers or if there were no negative numbers entered
- 
"""

sum_negative = 0
sum_positive = 0
quantity_positive = 0
quantity_negative = 0
quantity_zero = 0

for i in range(10):
    while True:
        try:
            num=int(input(f"Enter a positive or negative integer number {i+1}: "))
            
            if num>0:
                sum_positive+=num
                quantity_positive += 1
                break
                
            elif num<0:
                sum_negative+= abs(num)
                quantity_negative += 1
                break
            else:
                quantity_zero == 0
                break

        except ValueError:
            print("Please, enter a interger number!")

"""def is_there_positive():
    if quantity_positive == 0:
        print("There is no positive number!")
    elif quantity_negative == 0:
        print("There is no negative number!")"""

def avarage_of_positive_number():
    if quantity_positive == 0: 
        print("There is no positive number!")
    elif quantity_positive != 0:
        avarage_positive = sum_positive / quantity_positive
        print(f"The avarage of positive numbers is: {round(avarage_positive, 2)}") 

def avarage_of_negative_number():
    if quantity_negative == 0:
        print("There is no negative number!")
    elif quantity_negative != 0:
        avarage_negative = sum_negative / quantity_negative
        print(f"The avarage of negative numbers is: {round(avarage_negative, 2)}")
            

print(f"The sum up of positive numbers is: {sum_positive}")
print(f"The sum up of negative numbers is: {sum_negative}")

avarage_of_positive_number()
avarage_of_negative_number()

