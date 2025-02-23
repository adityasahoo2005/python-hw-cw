''' Accept marks of three subjects. Print total and average along with whether a candidate has
passed or fail. If student secures <= 39 marks in any subject, consider him as fail. Also assigned a
subject wise grade based on the following table:
Marks Range Grade
Absent NA
0 – 39 F
40 – 44 P
45 – 49 C
50 – 54 B
55 – 59 B+
60 – 69 A
70 – 79 A+
80 – 100 O '''



def get_grade(marks):
    if(80<=marks<=100):
        return("O")
    elif(70<=marks<=79):
        return("A+")
    elif(60<=marks<=69):
        return("A")
    elif(55<=marks<=59):
        print("B+")
    elif(50<=marks<=54):
        return("B")
    elif(45<=marks<=49):
        return("C")
    elif(40<=marks<=44):
        return("P")
    else:
        return("F")                           
marks1 = int(input("enter the marks of subject 1 : "))
marks2 = int(input("enter the marks of subject 2 : "))
marks3 = int(input("enter the marks of subject 3 : "))
total = marks1 + marks2 + marks3
average = (marks1 + marks2 + marks3)/3
print("total marks of three subjects are : ", total)
print("average marks of three subjects are : ", average)
if(marks1>39 and marks2>39 and marks3>39):
    print("Congrats!!! You passed in all three subjects")
    print("Here are your grade according to your marks in each subjects")
else:
    print("Sorry!!! You are failed better luck next time")
    print("Here are your grade according to your marks in each subjects")    
grade1 = get_grade(marks1)
grade2 = get_grade(marks2)
grade3 = get_grade(marks3)
print("Marks and grade of subject 1 ", marks1,"and", grade1,)
print("Marks and grade of subject 2 ", marks2,"and", grade2,)
print("Marks and grade of subject 3 ", marks3,"and", grade3,)