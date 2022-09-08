a=int(input("enter the number:"))
org=a
b=0
while(a>0):
    x=a%10
    b=b*10+x
    a=a//10
print("reverse of number:",b)
