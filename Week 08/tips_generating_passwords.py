import string
import random

letters = string.ascii_letters  # Alphabet letters upper & lowercase
digits = string.digits  # All numbers 0-9
symbols = string.punctuation  # All special characters/symbols

characters_combo = ""
combo_length = input("Enter the length (press enter for 10): ")
if combo_length == "":
    combo_length = 10
else:
    combo_length = int(combo_length)
for character in range(combo_length):
    characters_combo += random.choice(letters)

print(characters_combo)
include_digits = input("Would you like to include digits? [y/n]: ").lower()
if include_digits == "n":
    use_digits = False
else:
    use_digits = True

if use_digits:
    characters_combo += digits
print(characters_combo)
