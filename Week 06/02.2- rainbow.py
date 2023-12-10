month_list = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
rainfall_data = []
count = 0
while count < 12:
    try:
        num = int(input(f'Enter the amount of rainfall of {month_list[count]}: '))
        rainfall_data.append(num)
        count += 1
    except:
        print("Input not accepted.")
highNum = max(rainfall_data)
blank = "   "
star = " * "
for x in range(highNum):
    for y in range(len(rainfall_data)):
        if y == 11:
            if (rainfall_data[y] - highNum) < 0:
                print(blank)
                highNum = highNum - 1
            else:
                print(star)
                highNum = highNum - 1
        else:
            if (rainfall_data[y] - highNum) < 0:
                print(f'{blank} ', end="")
            else:
                print(f'{star} ', end="")
print(" ".join(month_list))


