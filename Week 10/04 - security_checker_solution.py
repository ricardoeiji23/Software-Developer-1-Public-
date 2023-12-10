import json #Provides methods for working with JSon data

def display_menu(): #Print a simple menu for the user 
    print("1. New user")
    print("2. Existing user")
    print("3. Exit")

def create_new_user(): #Create new "username" and "password"
    username = input("Enter a username: ")

    # Validate and set a new password
    while True:
        password = input("Enter a new password (At least 8 characters): ")
        if (
            len(password) >= 8
            and not password.startswith(' ')
            and not password.endswith(' ')
            and not password[0].isdigit()
        ):
            confirm_password = input("Confirm the password: ")
            if password == confirm_password:
                # Save user details to JSON file
                user_data = {'username': username, 'password': password} #Create a dictionary with the 2 variables
                with open('04 - user_credentials.json', 'a') as file: #Defining the code into "file" #Will open the JSon file with the "Append mode" to add content in the final
                    json.dump(user_data, file) #Convert and add the Python Dictionary "user_data" to the JSON file "file"
                    file.write('\n') #Add a newline character
                print("User created successfully!")
                break
            else:
                print("Passwords do not match. Please try again.")
        else:
            print("Invalid password. Please try again.")

def existing_user_login(): #When call it, the variables will be reset
    username = input("Enter your username: ") #Ask for the username
    password_attempts = 3 #Times that it can try

    # Check username/password against entries in the JSON file
    while password_attempts > 0: #While the "password_attempts" is not equal 0
        password = input("Enter your password: ") #Input the password
        try:
            with open('04 - user_credentials.json', 'r') as file: #Variable file will be in the "read mode"
                for line in file: #For each line in file
                    user_data = json.loads(line) #checks if the entered username and password match any of the entries in the file.
                    if user_data['username'] == username and user_data['password'] == password: #Access to the value associated with the key #If the username(key) in the JSon is the same of the input
                        print("Welcome, {}!".format(username))
                        return #Used to exit the function
                print("Incorrect username or password. Attempts left: {}".format(password_attempts - 1))
        except json.JSONDecodeError:
            print("Error reading user credentials. Please contact support.")
            break
        password_attempts -= 1 #If it doesn't hit the "Return" it'll count the attempts

    print("You are locked out. Please contact support.")

def main():
    while True:
        display_menu()
        choice = input("Select an option (1, 2, or 3): ")

        if choice == '1':
            create_new_user()
        elif choice == '2':
            existing_user_login()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
