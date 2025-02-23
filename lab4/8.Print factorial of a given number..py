# Function to calculate factorial of a given number
def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Accepting the number from the user
number = int(input("Enter a number: "))

# Calculating the factorial
result = calculate_factorial(number)

# Printing the result
print(f"The factorial of {number} is: {result}")
