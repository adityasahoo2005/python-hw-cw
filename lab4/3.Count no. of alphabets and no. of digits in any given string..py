def count_alphabets_and_digits(s):
    alphabets = 0
    digits = 0
    
    for char in s:
        # Check if the character is an alphabet
        if ('A' <= char <= 'Z') or ('a' <= char <= 'z'):
            alphabets += 1
        # Check if the character is a digit
        elif '0' <= char <= '9':
            digits += 1
    
    return alphabets, digits

# Accepting the string from the user
user_input = input("Enter a string: ")

alphabets_count, digits_count = count_alphabets_and_digits(user_input)

print(f"The number of alphabets in the string is: {alphabets_count}")
print(f"The number of digits in the string is: {digits_count}")
