
# Check whether it is a leap year or not

# Accept a year value from the user
year = int(input("Enter a year: "))

# Check if the year is a leap year or not
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(" Your entered year : " ,year, "is a leap year.",)
else:
    print(" Your entered year : " ,year, "is not a leap year.")
