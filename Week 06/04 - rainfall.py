# Create a list to store monthly rainfall data
rainfall_data = []

# Prompt the user for monthly rainfall data
for month in range(1, 13):
    while True:
        try:
            rainfall = float(input(f"Enter rainfall (mm) for month {month}: "))
            if 100 >= rainfall >= 0:
                rainfall_data.append(rainfall)
                break
            else:
                print("Rainfall should be a non-negative value.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Determine the maximum rainfall to scale the histogram
max_rainfall = max(rainfall_data)

# Create a vertical histogram
print("\nRainfall Histogram (Vertical):")

for i in range(40, 0, -1): #Start. stop, step
    row = "" #Used to create a and build the content of the row
    for rainfall in rainfall_data:
        if int(40 * (rainfall / max_rainfall)) > i:
            row += "#\t"
        else:
            row += "\t"
    print(row) #print each vertical row

# Print the month labels
print("\nJan\tFeb\tMar\tApr\tMay\tJun\tJul\tAug\tSep\tOct\tNov\tDec")

