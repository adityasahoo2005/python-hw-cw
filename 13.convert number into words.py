# Convert number 0 to 19 to its equivalent words. E.g. 0 → zero, 19→nineteen.

def convert_numbers_to_words(number):
    if number < 0 or number > 19:
        return "Invalid Inputs please enter number between 0 and 19."
    
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
             "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
             "seventeen", "eighteen", "nineteen"]
            
    return words[number]

# Take input from user
number=int(input("Enter A Number Between 0 and 19 : "))
print(convert_numbers_to_words(number))