a=[]
ele=int(input("enter the no of words:"))
for i in range(ele):
    words=input("enter the words:")
    a.append(words)
a.sort()
order=input("Order(A/D):")
if order=="A":
    for i in a:
        print(i)
elif order=="D":
    a.sort(reverse=True)
    for i in a:
        print(i)
else:
    print("Invalid Input")
