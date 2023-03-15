import random
import string
import time

random_number = random.randint(1, 100)  # Generate a random number between 1 and 100
print("Random number:", random_number)

letters = string.ascii_letters  # Alphabet letters upper & lowercase
digits = string.digits  # All numbers 0-9
symbols = string.punctuation  # All special characters/symbols
characters_combo = letters + digits + symbols  # Add all

print("Letters:", letters)
print("Digits:", digits)
print("Symbols:", symbols)
print("Characters Combo:", characters_combo)

random_letter = random.choice(letters)  # Pick a random letter from letters
random_digit = random.choice(digits)  # Pick a random digit from digits
random_symbol = random.choice(symbols)  # Pick a random symbol from symbols
random_characters_combo = random.choice(characters_combo)  # Pick a random character

print("Random letter:", random_letter)
print("Random digit:", random_digit)
print("Random symbol:", random_symbol)
print("Random character:", random_characters_combo)

character_limit = 50
my_magical_word = ""
for character in range(character_limit):
    my_magical_word += random.choice(digits + symbols)
print("My magical word:", my_magical_word)

print("Im quick")
print("Processing...")
time.sleep(2)  # Delay by 2 seconds
print("I've taken my time")
print("I'm done")

print("Processing next phase")
for i in range(10):
    time.sleep(1)
    print(f"\r{(i*10)+10}%", end="")
print("\nComplete!")
