usernames = []
phones = []
file_in = open("phonebook.txt", "r")
for line in file_in:
    usernames.append(line.split(" ")[0])
    phones.append(line.split(" ")[1])
print(phones)
entered_name = input("Enter name: ")
entered_phone = input("Enter phone: ")
if entered_name in usernames and entered_phone == phones[usernames.index(entered_name)]:
    print("Successful Login!")
else:
    print("Invalid.")
