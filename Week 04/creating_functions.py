def greet():
    print("Hello")

greet()
def get_name_and_greet():
    name = input("Enter your name: ")
    print("Hello", name)

get_name_and_greet()
def verify_age():
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You're an adult")
    else:
        print("You're a minor")


verify_age()


# Using return

def is_successful(result):
    if result >= 50:
        return True
    else:
        return False


my_result = int(input("Enter your result: "))
if is_successful(my_result):
    print("You've been successful")
else:
    print("Sorry, you haven't been successful")


def multiply_by_five(number):
    return 5 * number


entered_number = int(input("Enter a number to multiply it by 5: "))
print(multiply_by_five(entered_number))
