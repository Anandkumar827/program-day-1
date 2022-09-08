n=int(input("Enter the no:of rows:"))
for i in range(n):
    for j in range(1,n- i):
        print(" ", end="")
    for k in range(i + 1):
        print(k + 1, end=" ")
    print()
