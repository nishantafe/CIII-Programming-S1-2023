MENU = "l) Login, S) Sign up, q) Quit"

done = False
while not done:
    print(MENU)
    user_choice = input("Choose [l/s/q]: ").lower()
    if user_choice == "l":
        print("Logging you in...")
    elif user_choice == "s":
        print("Signing you up...")
    elif user_choice == "q":
        done = True
        print("Quitting the program....")
    else:
        print("Invalid choice.")
