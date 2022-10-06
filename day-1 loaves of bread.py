a=int(input("Enter the number of fresh loaves:"))
b=int(input("Enter the number of day old loaves:"))
a=a*185
b=b*185
if(a>0 and b>=0):
    print("the regural price of loaves:185/-")
    print("the amount of new loaves is :%0.2f"%(a))
    print("the amount of day old loaves is:%0.2f"%(b*0.6))
    print("the total amount:%0.2f"%(a+(b*0.6)))
else:
    print("invalid input")
