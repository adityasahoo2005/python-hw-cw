#Given the coordinates (x,y) of center of a circle and its radius, determine whether a point lies
#inside the circle, on the circle or outside the circle. (Hint: Use sqrt( ), pow( ) )

import math

def circle_properties(x_center, y_center, radius, x_point, y_point):
    distance = math.sqrt(pow(x_point - x_center, 2) + pow(y_point - y_center, 2))
    if distance < radius:
        return "Point lies inside the circle."
    elif distance == radius:
        return "Point lies on the circle."
    else:
        return "Point lies outside the circle."

x_center = float(input("Enter the x-coordinate of the center of the circle: "))
y_center = float(input("Enter the y-coordinate of the center of the circle: "))

radius = float(input("Enter the radius of the circle: "))

x_point = float(input("Enter the x-coordinate of the point: "))
y_point = float(input("Enter the y-coordinate of the point: "))

result = circle_properties(x_center, y_center, radius, x_point, y_point)

print(result)
