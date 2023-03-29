phonebook_dictionary = {}


def read_into_dictionary():
    file_in = open("phonebook.txt", "r")
    for line in file_in:
        name, phone = line.split(" ")
        phonebook_dictionary[name] = phone.rstrip()


# Find if a name exists in the names
a_name = input("Enter a name to check if it exists: ")
if a_name in phonebook_dictionary.keys():
    print(a_name, "exists and his/her phone is", phonebook_dictionary[a_name])
else:
    print(f"No record of {a_name} is found")


# Validate a name and a phone number
def validate_account():
    read_into_dictionary()
    print("\nName & Phone Validation")
    entered_name = input("Enter a name: ")
    entered_phone = input("Enter the phone number: ")
    if entered_name in phonebook_dictionary.keys() and entered_phone == phonebook_dictionary[entered_name]:
        print("That is a valid record!")
    else:
        print("No such record exists.")


validate_account()
