print("Enter the principal amount:")
p=int(input())
print("Enter the number of years:")
t=float(input())
print("Is the customer is senior citizen :(Y/N)")
ch=(input())
if(ch=="Y"):
    r=12
else:
    r=10
SI=(p*t*r)/100
print("simple intrest:",SI)
