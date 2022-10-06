import math
a=int(input("n="))
b=[]
if(a<1):
    print("enter a valid number")
else:
    print("Factorial =",math.factorial(a))
for i in range(1,a+1):
    if a%i==0:
        b.append(i)
print("Number of factors for:",len(b))
