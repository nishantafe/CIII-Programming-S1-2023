# Student name:
# Date:
"""Welcome to Simple Login program"""

import random
import string
import time

# Create menu items message
MENU = "a) Login	b) Create an account	c) View accounts	d) Quit"

accounts = {}
file_in = open("accounts.txt", "r")


def read_file():
    for line in file_in:
        # store key and value after extracting them by splitting using a space
        key, value = line.split(" ")

        # add and associate the key to a value in the dictionary
        # use value.rstrip() to clean up spaces or new lines before & after each value.
        accounts[key] = value.rstrip()


def login():
    try_again = True
    while try_again:

        print("Login\n-----")
        username = input("Username: ")
        password = input("Password: ")
        print("\nProcessing...")
        time.sleep(1)

        if (username in accounts) and (password == accounts[username]):
            print("You have successfully logged in.")
            try_again = False

        else:
            print("Password incorrect.")
            reattempt = input("Would you like to try again? [y]/n: ").lower()
            if reattempt == "n":
                try_again = False
            else:
                try_again = True


def view_accounts():
    print("\nList of all accounts\n--------------------------")
    for username, password in accounts.items():
        print("{:15s} {}".format(username, password))


def create_account():
    print("\nCreate an account\n------------------")
    unique_username = False
    existing_usernames = accounts.keys()

    while not unique_username:
        new_username = input("Username: ")
        if new_username in existing_usernames:
            print("Sorry, that username is unavailable. Please try a different one.")
            unique_username = False
        else:
            unique_username = True
            print("\nWould you like to:\n"
                  "A) Create your own password\n"
                  "B) Randomly generate a password")

            password_style = input("\nChoose [a/b]: ").lower()
            new_password = ""
            if password_style == "a":
                new_password = input("\nEnter password: ")

            elif password_style == "b":
                print("\nLet's create a unique password for you...")

                include_digits = input("Would you like your password "
                                       "to include numbers? [y]/n: ").lower()
                if include_digits == "n":
                    use_digits = False
                else:
                    use_digits = True

                include_symbols = input("\nWhat about symbols? [y]/n: ").lower()
                if include_symbols == "n":
                    use_symbols = False
                else:
                    use_symbols = True

                chosen_length = input("\nLength of the password [10]: ")
                if chosen_length == "":
                    password_length = 10
                else:
                    password_length = int(chosen_length)

                letters = string.ascii_letters
                digits = string.digits
                symbols = string.punctuation

                confirmed_characters = letters
                if use_digits:
                    confirmed_characters += digits
                if use_symbols:
                    confirmed_characters += symbols
                generated_password = ""
                for length in range(password_length):
                    generated_password += random.choice(confirmed_characters)
                new_password = generated_password

            print("\nYour account has been created.")
            print("You can now log in.")
            print("username:", new_username, "\npassword:", new_password)
            file_out = open("accounts.txt", "a")
            new_account = new_username + " " + new_password
            file_out.write(new_account + "\n")
            file_out.close()


def get_user_choice():
    # Display menu items
    print("\n", MENU)
    # Get the user choice
    user_choice = input("Choose [a/b/c/d]: ").lower()
    if user_choice == "a":
        login()
    elif user_choice == "b":
        create_account()
    elif user_choice == "c":
        view_accounts()
    return user_choice


read_file()
while get_user_choice() != "d":
    get_user_choice()
else:
    print("Quitting program...")
    file_in.close()
    time.sleep(2)
