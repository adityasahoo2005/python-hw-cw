# Function to print N natural numbers in reverse
def print_reverse_natural_numbers(n):
    for i in range(n, 0, -1):
        print(i, end=" ")

# Accepting the value of N from the user
N = int(input("Enter the value of N: "))

# Printing the numbers in reverse order
print_reverse_natural_numbers(N)
