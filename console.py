from datetime import datetime
import re
users = []

def is_password_valid(password):
    if 8 <= len(password) <= 15:
        if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) and re.search(r'\d', password) and re.search(r'[!@#$%^&*]', password):
            return True
    return False

def get_dob():
    while True:
        dob_str = input("Enter your date of birth (yyyy-MM-dd): ")
        try:
            dob = datetime.strptime(dob_str, "%Y-%m-%d")
            return dob
        except ValueError:
            print("Invalid date format. Please enter a valid date.")

def is_username_email(username, email):
    for user in users:
        if user[0] == username or user[1] == email:
            return False
    return True

def encrypt_password(password):
    s = ""
    for i in password:
        s += (i + "3")
    return s

def signup():
    print("========================================================")
    print("                 User Sign-up")
    username = input("Enter a username: ")
    email = input("Enter an email: ")

    if not is_username_email(username, email):
        print("Username or email already exists. Please choose different ones.")
        

    password = ""
    while not is_password_valid(password):
        password = input("Enter a password: ")

        if not is_password_valid(password):
                    print("Password does not meet the requirements. Please try again.")

    dob = get_dob()

        
    users.append((username, encrypt_password(password), email, dob))
    print(users)
    print("User registered successfully!")
    print("=========================")
    print()

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for user in users:
        if user[0] == username and user[1] == encrypt_password(password):
            print("Login successful!")
            return

    print("Login failed. Please try again.")

def forgotpassword():
    s = input("Enter your Email:")
    for i in range(len(users)):
        if s == users[i][2]:
            new_password = input("Enter your new password:")
            if new_password != users[i][0] and new_password != users[i][1] and is_password_valid(new_password):
                users[i] = (users[i][0], encrypt_password(new_password), users[i][2], users[i][3])
                print("Password updated successfully!")
                return

    print("Email not found or invalid password. Please try again.")

while True:
    t = int(input("Enter your choice:"))
    if t == 1:
        signup()
    elif t == 2:
        login()
    elif t == 3:
        forgotpassword()


        

