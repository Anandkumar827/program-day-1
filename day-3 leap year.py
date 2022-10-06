year=int(input("enter year:"))
if(year>0):
    if(year%4==0 or year%400==0):
        print("it is a leap year")
    else:
        print("it is not a leap year")
        if(year%4!=0):
            year-=int(year%4)
        print("leap year:",year)
else:
    print("not valid")
