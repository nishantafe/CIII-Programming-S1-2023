MENU = "l) Login, S) Sign up, q) Quit"


def get_user_choice():
    print(MENU)
    user_choice = input("Choose [l/s/q]: ").lower()
    if user_choice == "l":
        print("Logging you in...")
    elif user_choice == "s":
        print("Signing you up...")

    return user_choice


while get_user_choice() != "q":
    get_user_choice()
else:
    print("Quitting the program....")
