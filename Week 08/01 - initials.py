full_name = input("Enther your full name (First and family): ")

names = full_name.split() #Each space it going to be a seperate string

if len(names) >= 2:
    first_initial = names[0][0].upper() #First item #Character 0
    last_initial = names[-1][0].upper() #Last item #Character 0

    print(f"\nYour initials are:{first_initial}.{last_initial}")

else:
    print("Please, enter both a first and a family name")