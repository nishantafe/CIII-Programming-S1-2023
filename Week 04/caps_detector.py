"""This program will detect any capital letter in a user's entry and display a message"""
word = input("Enter a word: ")
if "n" in word:
    print("n was found")

caps_count = 0
for char in word:
    if char == char.upper():
        caps_count += 1
if caps_count > 0:
    print("At least 1 capital letter was found")
else:
    print("No capital letter(s) was found")
