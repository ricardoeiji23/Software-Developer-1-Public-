

while True:
    rows = int(input("Enter a positive number: "))
    for i in range(rows):
        print(" " * (rows - i) + " *" * (i + 1)) 
            # Space num: 5 - 1 = 4 spaces then it decreases (5-2=3, 5-3=2)
            # row: 5
            # i: 1, 2, 3, 4, 5... 
            # Stars num: 0+1=1, 1+1=2, 2+1=3...

    for j in range(rows):
        print(" " * (j + 2) + " *" * (rows - 1 - j))
        # Now we are doing the other half of the dimond
        # J: 0, 1, 2, 3, 4...
        # Space num: j + 2 (1 + 2 = 3 > 4 > 5)
        # Stars: rows (5 - Start with full) - 1 (To adjust the alignment) - J (0, 1, 2, 3, 4) (J because it'll decrese 1 star)
            # Start with full and will be decreasing 1 start 

    