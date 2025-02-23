# Check whether a triangle is valid or not, when the three angles of the triangle are entered through the keyboard. A triangle is valid if the sum of all the three angles is equal to 180 degrees


# Accept the three angles of the triangle from the user
angle1 = int(input("Enter the first angle of the triangle: "))
angle2 = int(input("Enter the second angle of the triangle: "))
angle3 = int(input("Enter the third angle of the triangle: "))

# Check if the sum of all three angles is equal to 180 degrees
if angle1 + angle2 + angle3 == 180:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")
