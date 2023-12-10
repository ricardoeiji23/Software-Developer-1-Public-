"""
- 1 foot = 3.048 decimeters
- 1 inch = 2.54 centimeters
- 1 foot = 12 inches 

Plan
    Ask for the inputs
    Calculate the total of inches (Feet + inches)
        Transform the feet into inches (Always focus on the smallest measurement)
    Covert the result measurements into inches (division)
    Calculate the values of the measurement results multiplying the total inches with the inches of the measurements


Plan test
    5 feet + 10 inches = 1.778 meters 

"""

def height_converter(): #Create the function
    #Ask for the inputs
    feet = float(input("Enter your height in feet: "))
    inches = float(input("Enter your height in inches: "))

    #Get the total of inches of the input
    total_inches_input = feet * 12 + inches

    #See how much a inche represent in km, m, cm, mm
    inches_in_km = 0.0000254
    inches_in_m = 0.0254
    inches_in_cm = 2.54
    inches_in_mm = 25.4

    #Calculate the total inches with the "inches in km, m, cm, mm"
    heigh_km = total_inches_input * inches_in_km
    heigh_m = total_inches_input * inches_in_m
    heigh_cm = total_inches_input * inches_in_cm
    heigh_mm = total_inches_input * inches_in_mm

    #Print the values of the height with the correct conversion
    print(f"\nHeight in kilometers: {heigh_km}")
    print(f"\nHeight in meters: {heigh_m}")
    print(f"\nHeight in Centimeters: {heigh_cm}")
    print(f"\nHeight in millimeters: {heigh_mm}")

# Call the function
height_converter()