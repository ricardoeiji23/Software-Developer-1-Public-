def print_caractere(caractere, num): #Create a seperate function to print the caracter
    print(caractere * num) #Multiply the number of prints of the caractere

def main():
    while True:
        try:
            num=int(input("Input a posivite number (Or '0' to end): ")) #Ask the positive number

            if num == 0:
                print("Program finished\n")
                break #Finish the function and program 

            if num <= 0:
                print("Please, enter a positive number!\n")
                continue #it'll ignore the rest and go back to the begin of the program

            caractere = input("Enter just a single caracter of text: ") #Ask the caracter text

            if len(caractere) != 1:
                print("Please, enter just 1 caracter of text!\n")
                continue
            
            print_caractere(caractere, num) #call the function 

            print("\n")

        except ValueError:
            print("Enter only a integer number!!!\n")


if __name__ == "__main__":
    main()
