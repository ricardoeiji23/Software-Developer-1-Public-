"""
- 1 Hour = 3600 seconds
- The quantity of minutes = rest of the seconds (not exact division rest) // 60 (1 min = 60 seconds)
- The quantity of seconds = rest of the seconds from the minutes (Now is just the seconds)
"""

number = int(input("Enter a positive number of the seconds: "))

print("\n")

hour = number//3600 #Calculating the number of hours (Diving by 3600)
r_hour = number%3600 #Calculating the resto of the seconds that remain/left 

minute = r_hour//60 #calculating the minutes 
r_minute = r_hour%60 #calculating the rest of the seconds that remain/left (It's the seconds)


second = r_minute

print("Input: ", str (number), "\n")
print("Hours: ", str(hour), "Hours", "\n")
print("Minutes: ", str(minute), "Minutes", "\n")
print("Seconds: ", str(second), "Seconds")

