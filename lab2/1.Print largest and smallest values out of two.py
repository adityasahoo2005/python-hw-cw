# Print largest and smallest values out of two.
a=int(input("Enter the first number :  "))
b=int(input("Enter the second number : "))

if (a>b):
    print("The largest number is : ",a)
    print("The smallest number is : ",b)

elif(b>a):
    print("The largest number is : ",b)
    print("The smallest number is : ",a)

else:
    print("Both numbers" , a, "and" , b, "are equals")
        