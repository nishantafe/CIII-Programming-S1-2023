x = input("hello")

while not type(x) is int:
  raise TypeError("Only integers are allowed")