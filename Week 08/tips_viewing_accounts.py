phonebook_dictionary = {}


def view_accounts():
    file_in = open("phonebook.txt", "r")
    for line in file_in:
        name, phone = line.split(" ")
        phonebook_dictionary[name] = phone.rstrip()
    print(f"{'Name':10s} Phone\n{'':-<21s}")
    for name, phone in phonebook_dictionary.items():
        print(f"{name:10s} {phone}")

# view_accounts()

user_choice = input("Enter v to view the accounts: ")
if user_choice.lower() == "v":
    view_accounts()
else:
    print("invalid choice.")
