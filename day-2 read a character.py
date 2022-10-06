upper=0
lower=0
count=0
arr=[]
print("ENTER * TO QUIT")
while(arr!='*'):
    arr=input("ENTER THE ELEMENT----> ")
    if(arr>='A' and arr<='Z'):
        upper+=1
    elif(arr>='a' and arr<='z'):
        lower+=1
    elif(arr>='0' and arr<='9'):
        count+=1
    if(arr=='!' and arr=='@' and arr=='#' and arr=='$' and arr=='%' and arr=='^' and arr=='&' and arr=='(' and arr==')' and arr=='_' and
       arr=='-' and arr=='+' and arr=='=' and arr=='~' and arr=='`'):
        print("SPECIAL CHARACTERS ARE NOT ALLOWDED")
        exit()
print("NUMBER OF UPPER CASE----> ",upper)
print("NUMBER OF LOWER CASE----> ",lower)
print("NUMBER OF NUMBERS----> ",count)
