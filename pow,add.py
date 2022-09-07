def pow(x,n):
    return(x**n)
def add(x,n):
    return(x+n)
def sub(x,n):
    return(x-n)
def mul(x,n):
    return(x*n)
def div(x,n):
    return(x/n)
m=int(input("select any operation:\n"
            "1.power\n"
            "2.addition\n"
            "3.subtraction\n"
            "4.multiplication\n"
            "5.division\n"))
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
if(m==1):
    print(a,"**",b,"=",pow(a,b))
elif(m==2):
    print(a,"+",b,"=",add(a,b))
elif(m ==3):
    print(a,"-",b,"=",sub(a,b))
elif(m==4):
    print(a,"*",b,"=",mul(a,b))
elif(m==5):
    print(a,"/",b,"=",div(a,b))
else:
    print("invalid input")

            
            

            
            
