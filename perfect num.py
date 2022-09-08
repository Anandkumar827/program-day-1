a=int(input("Enter the number:"))
b=0
for i in range(1,a):
    if(a%i==0):
        b+=i
if(b==a):
        print("perfect number")
else:
        print("Not perfect number")
