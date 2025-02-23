# Print 24 hours of day with suitable suffixes like AM, PM, Noon and Midnight.

def print_24_hours():
    for hour in range(24):
        if hour == 0:
            suffix = "Midnight"
        elif hour < 12:
            suffix = "AM"
        elif hour == 12:
            suffix = "Noon"
        else:
            suffix = "PM"
        
        formatted_hour = hour % 12
        formatted_hour = 12 if formatted_hour == 0 else formatted_hour
        
        if suffix == "Midnight":
            print("12 Midnight")
        elif suffix == "Noon":
            print("12 Noon")
        else:
            print(f"{formatted_hour} {suffix}")

# Calling the function to print 24 hours with suffixes
print_24_hours()
