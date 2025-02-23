# Print nCr and nPr

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def nPr(n, r):
    return factorial(n) // factorial(n - r)

# Accepting the values of n and r from the user
n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))

# Calculating nCr and nPr
combination = nCr(n, r)
permutation = nPr(n, r)

print(f"{n}C{r} = {combination}")
print(f"{n}P{r} = {permutation}")
