"""
ask for 2 inputs: 
    one for ROWS (width - Quantas larguras)
    one for COLUMNS (height - Quantas alturas)


    
"""
num_rows = int(input("Enter the number of rows: ")) 
num_columns = int(input("Enter the number of columns: "))
    # Ask the number of rows and columns
    # Defining the limit of the "FOR"


for rows in range(num_rows): # For rows in the limit range of the input (rows)
    for column in range(num_columns): # For comuns in the limit range of the input (colums)
        print("■", end = "  ") # alt + 254 = box # (end = "  ") - is to know how it ends for each print 
    print() # It goes to the next row