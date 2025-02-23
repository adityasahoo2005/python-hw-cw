# Count how many vowels are there in a string. Accept the string from the user.

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Accepting the string from the user
user_input = input("Enter a string: ")
vowel_count = count_vowels(user_input)

print(f"The number of vowels in the string is: {vowel_count}")
 
