#Given three points (x1,y1), (x2,y2) and (x3,y3), check if all the three points fall on one straight 
# line.

def are_points_collinear(x1, y1, x2, y2, x3, y3):
    # Calculate the slopes
    slope1 = (y2 - y1) * (x3 - x2)
    slope2 = (y3 - y2) * (x2 - x1)
    
    # Check if the slopes are equal
    return slope1 == slope2

# Take input from the user
x1, y1 = map(int, input("Enter the coordinates of the first point (x1 y1): ").split())
x2, y2 = map(int, input("Enter the coordinates of the second point (x2 y2): ").split())
x3, y3 = map(int, input("Enter the coordinates of the third point (x3 y3): ").split())

if are_points_collinear(x1, y1, x2, y2, x3, y3):
    print("The points are collinear.")
else:
    print("The points are not collinear.")































''' def are_points_collinear(x1, y1, x2, y2, x3, y3):
    # Calculate the slopes
    slope1 = (y2 - y1) * (x3 - x2)
    slope2 = (y3 - y2) * (x2 - x1)
    
    # Check if the slopes are equal
    if slope1 == slope2:
        return True
    else:
        return False

# Example usage
x1, y1 = 1, 2
x2, y2 = 2, 4
x3, y3 = 3, 6

if are_points_collinear(x1, y1, x2, y2, x3, y3):
    print("The points are collinear.")
else:
    print("The points are not collinear.") '''
