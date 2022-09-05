print("printing greatest number among three")
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
if(a<c):
    if(a<b)and (b>c):
        print(b,"number is greatest")
    else:
        print(c,"number is greatest")
else:
    print(a,"number is greatest")
