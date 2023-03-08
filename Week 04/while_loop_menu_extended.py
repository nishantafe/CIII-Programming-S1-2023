MENU = "l) Login, S) Sign up, q) Quit"
valid_username = "nishan"
valid_password = "password"


def login():
    print("Logging you in...")
    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")
    if entered_username == valid_username and entered_password == valid_password:
        print("Successful login")
    else:
        print("Invalid credentials.")


done = False
while not done:
    print(MENU)
    user_choice = input("Choose [l/s/q]: ").lower()
    if user_choice == "l":
        login()
    elif user_choice == "s":
        print("Signing you up...")
    elif user_choice == "q":
        done = True
        print("Quitting the program....")
    else:
        print("Invalid choice.")
