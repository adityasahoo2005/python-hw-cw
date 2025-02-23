# Generate all Pythagorean Triplets with side length <= 30.

def generate_pythagorean_triplets(limit):
    for a in range(1, limit + 1):
        for b in range(a, limit + 1):
            for c in range(b, limit + 1):
                if a**2 + b**2 == c**2:
                    print(f"({a}, {b}, {c})")

# Define the limit
limit = 30

# Generate and print Pythagorean triplets
generate_pythagorean_triplets(limit)
