list_nums = []

while True:
    try:
        num1 = int(input("Enter a positive or negative integer: "))
        num2 = int(input("Enter a positive or negative integer: "))

        list_nums.append(num1) #Add one by one
        list_nums.append(num2)

        print("The integers in the first lists are: ",list_nums)

        list_nums[0], list_nums[1] = list_nums[1], list_nums[0] #For swappig, it must be this or create a third value

        print("The new list is now: ",list_nums, "\n")

    except ValueError:
        print("Please, enter a integer value!!!\n")
        continue
