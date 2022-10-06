pn=0
pnn=0
nn=0
nnn=0
arr=[]
tot=0
print("ENTER -1 TO EXIT")
while(arr!=-1):
    arr=int(input("ENTER THE ELEMENTS---> "))
    if(arr==0):
        print("NEITHER POSITIVE NOR NEGATIVE")
    elif(arr>0):
        pn=pn+arr
        pnn+=1
        avg=pn/pnn
    else:
        nn=nn+arr
        nnn+=1
        average=nn/nnn
print("AVERAGE OF POISTIVE OF NUMBERS---> ",avg)
print("AVERAGE OF NEGATIVE NUMBERS---> ",average)
