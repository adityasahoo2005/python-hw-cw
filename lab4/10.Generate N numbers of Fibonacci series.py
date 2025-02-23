# Generate N numbers of Fibonacci series

def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fibonacci_series = [0, 1]
    for i in range(2, n):
        next_number = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_number)
    
    return fibonacci_series

# Accepting the value of N from the user
N = int(input("Enter the number of terms (N): "))

# Generating the Fibonacci series
fibonacci_series = generate_fibonacci(N)

# Printing the Fibonacci series
print(f"The first {N} numbers of the Fibonacci series are:")
print(fibonacci_series)
