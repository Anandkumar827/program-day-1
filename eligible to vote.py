age=int(input("enter the age:"))
if (age>=18):
    print("Eligible to vote")
elif(age>0 and age<18):
    print("Not eligible to vote\n",18-age,"years left to be elgible")
else:
    print("invalid input")
