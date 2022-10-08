n = int(input("max no.of time printed:"))
a= str(input("enter the charecter to be printed:"))
for i in range(1, n+1):
    for k in range(1, i+1):
        print(a, end="")
    print()
    
