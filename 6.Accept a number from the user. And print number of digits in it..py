# Accept a number from the user. And print number of digits in it.

# Accept a number from the user
number = input("Enter a number: ")

# Convert the number to a string and get its length
num_of_digits = len(str(number))

# Print the number of digits
print(f"The number of digits in {number} is {num_of_digits}.")
