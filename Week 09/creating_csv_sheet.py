# Get data from the user
product_name = input("Enter a product name:")
product_price = input("Enter the price:")
stock = input("Enter how many in stock:")

# Headers
headers = "Product Name,Price,Stock\n"

file_out = open("data.csv", "a")

# Ensure that headers do not exist before you write them
file_in = open("data.csv", "r")
if headers not in file_in:  # If headers do no exist
    file_in.close()
    file_out.write(headers)  # Add the headers since they don't exist
else:
    file_in.close()

# Write data
file_out.write(f"{product_name},{product_price},{stock}\n")  # Write the data to file
file_out.close()
