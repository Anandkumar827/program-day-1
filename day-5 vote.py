age=int(input("enter your age:"))
if (age>=18):
    print("your allowed to vote")
elif(age>0 and age<18):
    print("You are allowed to vote after",18-age,"years")
else:
    print("invalid input")
