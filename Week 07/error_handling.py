# name = "Nishan"

try:
    print(name)
except NameError:
    print("This variable name has not been defined yet!")

number = input("Enter a number: ")
try:
    number = int(number)
    print(number, "is a valid number.")
except ValueError:
    print("You did not enter a number!")
