# Print largest and smallest values out of three
print("Enter three different numbers")

a=int(input("Enter the first number :  "))
b=int(input("Enter the second number : "))
c=int(input("Enter the third number : "))

if (a>b and a>c):
    print("The largest number is : ",a)
    if (b<c):
        print("The smallest number is : ",b)

elif(b>a and b>c):
    print("The largest number is : ",b)
    if (a<c):
        print("The smallest number is : ",a)

elif(c>a and c>b):
    print("The largest number is : ",c)
    if (a<b):
        print("The smallest number is : ",a)

else:
    print("Please Check the input")

