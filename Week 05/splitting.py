"""You can use the split() method
to extract data based on a seperator (like space)"""

record = "John 0452302453"
name, phone = record.split(" ")
print("Hi", name, "your number is", phone)
