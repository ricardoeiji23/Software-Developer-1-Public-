# A can covers 5.1m2 
# Each can has a diameter = 15cm and the height = 30cm (radious = diameter/2)
# box = 60 x 30 x 35cm (Largura, comprimento e altura)

"""
1
	floor: 40x30m 
    ceilin is 3.4m
    
    Wall_1 is (40*3.4)*2
    Wall_2 is (30*3.4)*2

    PS: He just wanna the 4 walls (30 * 3.4) and (40 * 3.4)
    
    To get the exact division with an int number, we need to use "//"
    
    We need to divide the total wall area with the paint can area to see how many cans we need 
    
2
    We need to find out the total number of cans and then we calculate how many boxes 

    1 - Find out the total number of paint cans 
    2 - Calculate the total volume of a cylinder: pi*radious^2*height
    3 - Divide the number of the area 

3
    Find out the number of cans not packed into boxes 
    
    Find out the full boxes and the rest of cans 

    Ps: Converte everything to meter  

"""

# Base information:

import math

can_paint_area = 5.1  # Square meters

can_diameter = 15 / 100  # Convert to meters (cm -> m)
can_height = 30 / 100  # Convert to meters (cm -> m)
can_radious = can_diameter / 2 

box_length = 0.60  # meters
box_width = 0.30  # meters
box_height = 0.35  # meters

box_volume = box_length * box_width * box_height

# Question 1

    # Floor = 40x30 
    # Height = 3.4 

Wall_1 = (40 * 3.4) * 2  # Square meters

floor_and_ceiling = (40*30)*2

total_area_Q1 = Wall_1 + floor_and_ceiling # Total area of two walls in square meters

minimum_number_of_cans = math.ceil(total_area_Q1 / can_paint_area) #We need one number higher to make sure of the number of cans

print("1 - The minimum number of cans necessaries is:", int(minimum_number_of_cans), "cans")

# Question 2 

can_volume = float(math.pi * (can_radious*can_radious) * can_height)

full_boxes = math.floor((minimum_number_of_cans * can_volume) / box_volume)

print("2 - The total number of full boxes is" ,full_boxes, "boxes")

# Question 3

cans_per_box = math.floor(minimum_number_of_cans / full_boxes) 

cans_not_packed = (minimum_number_of_cans%cans_per_box) # We calculate how many cans we have, divide with the number of cans per box and see the rest of cans 

print("3 - The number of cans not packed is", cans_not_packed, "cans\n")
