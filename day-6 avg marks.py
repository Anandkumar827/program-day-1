print("enter the marks obtained in the 4 subject")
a=int(input("Enter the marks in python:"))
b=int(input("Enter the marks in c programming:"))
c=int(input("Enter the marks in mathrmatics:"))
d=int(input("Enter the marks in pysics:"))
total=a+b+c+d
avg=total/4
print("the total marks:",total)
print("the avg marks:",avg)
if (avg>75):
    print("Distinction")
elif avg>=60 and avg<75:
    print("first division")
elif avg>=50 and avg<60:
    print("second division")
elif avg>=40 and avg<50:
    print("third division")
else:
    print("invalid input")
