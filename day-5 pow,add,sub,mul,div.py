def pow(m,n):
    return(m**n)
def add(m,n):
    return(m+n)
def sub(m,n):
    return(m-n)
def mul(m,n):
    return(m*n)
def div(m,n):
    return(m/n)
b=int(input("select any operation:-\n"
            "1.power\n"
            "2.addition\n"
            "3.subtraction\n"
            "4.multiplication\n"
            "5.division\n"))
a1=int(input("Enter the first number:"))
a2=int(input("Enter the second number:"))
if(b==1):
    print(a1,"**",a2,"=",pow(a1,a2))
elif(b==2):
    print(a1,"+",a2,"=",add(a1,a2))
elif(b==3):
    print(a1,"-",a2,"=",sub(a1,a2))
elif(b==4):
    print(a1,"*",a2,"=",mul(a1,a2))
elif(b==5):
    print(a1,"/",a2,"=",div(a1,a2))
else:
    print("invalid input")
