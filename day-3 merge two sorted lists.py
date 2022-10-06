a=int(input("Enter length of list1:"))
c=[]
for i in range(a):
    e=int(input("Enter element :"))
    c.append(e)
b=int(input("Enter length of list2:"))
d=[]
g=[]
for i in range(b):
    f=int(input("Enter element :"))
    d.append(f)
g=c+d
print("MERGED LIST :",sorted(g))
