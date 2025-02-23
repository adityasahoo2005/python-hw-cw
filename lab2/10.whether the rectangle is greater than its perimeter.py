#given the length and breadth of a rectangle, write a program to find whether the are of the 
#rectangle is greater than its perimeter

# Take input
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

area = length * breadth
perimeter = 2 * (length + breadth)


if  area > perimeter:
    print("The area of the rectangle is greater than its perimeter.")
else:
    print("The area of the rectangle is not greater than its perimeter.")
