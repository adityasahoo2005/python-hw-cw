# Function to print the multiplication table of a given number
def print_multiplication_table(number):
    for i in range(1,11):
        print(f"{number} x {i} = {number * i}")

# Accepting the number from the user
user_input = int(input("Enter a number: "))

print_multiplication_table(user_input)
