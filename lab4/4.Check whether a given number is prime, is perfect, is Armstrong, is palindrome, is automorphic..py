#Check whether a given number is prime, is perfect,
#is Armstrong, is palindrome, is automorphic.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n <= 0:
        return False
    sum_divisors = sum(i for i in range(1, n) if n % i == 0)
    return sum_divisors == n

def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    sum_digits = sum(int(digit) ** num_digits for digit in num_str)
    return sum_digits == n

def is_palindrome(n):
    num_str = str(n)
    return num_str == num_str[::-1]

def is_automorphic(n):
    square = n ** 2
    return str(square).endswith(str(n))

# Accepting the number from the user
number = int(input("Enter a number: "))

print(f"Is {number} prime? {is_prime(number)}")
print(f"Is {number} perfect? {is_perfect(number)}")
print(f"Is {number} Armstrong? {is_armstrong(number)}")
print(f"Is {number} palindrome? {is_palindrome(number)}")
print(f"Is {number} automorphic? {is_automorphic(number)}")
