
def get_rainfall_data(): #Function that will prompt the user for rainfall data to each month
    rainfall_data = [] #Monthly rainfall data will be stored
    months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ] # Prompt to the user when used the "for" loop to show each item in the list 

    for month in months:
        rainfall = float(input(f"Enter rainfall for {month} (in millimeters): ")) # For each month, ask for the input of the users
        rainfall_data.append((month, rainfall)) 
            # Add the month from the list + The input from the user 
            # Tp append 2 variables, must put them in ( ) -> For calling them, must call 2 variables 

    return rainfall_data #Return the list with with the 2 datas (Months and user)

def print_histogram(rainfall_data): 
    print("\nRainfall Histogram:")
    for month, rainfall in rainfall_data:
        print(f"{month}: {'*' * int(rainfall)}")

def main():
    print("Enter monthly rainfall data:")
    rainfall_data = get_rainfall_data()
    print_histogram(rainfall_data)

if __name__ == "__main__":
    main()
