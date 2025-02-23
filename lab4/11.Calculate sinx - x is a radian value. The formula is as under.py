#Calculate sin(x); x is a radian value. The formula is as under:
#sin⁡〖x=x- x^3/3!〗+ x^5/5!- x^7/7!…
#(hint: degrees can be converted into radians by 3.14159 / 180.)

import math

def sine(x, terms=10):
    sin_x = 0
    for n in range(terms):
        term = ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
        sin_x += term
    return sin_x

# Convert degrees to radians if necessary
def degrees_to_radians(degrees):
    return degrees * (3.14159 / 180)

# Example usage
x_degrees = 30  # Replace this with your desired angle in degrees
x_radians = degrees_to_radians(x_degrees)
result = sine(x_radians)
print(f"sin({x_degrees} degrees) = {result}")
