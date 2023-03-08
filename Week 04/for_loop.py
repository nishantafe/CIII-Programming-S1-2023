cars = ["BMW", "Mercedes", "Ford"]

for car in cars:
    print("Car:", car)

for time in range(2):
    print("How are you?\nI'm fine")

# print a letter 50 times
for character in range(8):
    print("x", end="")

# n, i and uppercase detector
word = input("\nEnter a word: ")
for letter in word:
    if letter == letter.upper():
        print("An upper case was detected")
    if letter == "n":
        print("The letter n was found in your word")
    if letter == "i":
        print("The letter i was found in your word")



