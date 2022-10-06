rows = int(input("Enter the no of rows : "))
column = int(input("Enter the no of Columns: "))

print("Enter the elements of Mat1:")
mat_a = [[int(input()) for i in range(column)] for i in range(rows)]
print("Mat1: ")
for n in mat_a:
    print(n)

print("Enter the elements of Mat2:")
mat_b = [[int(input()) for i in range(column)] for i in range(rows)]
print("Mat2: ")
for n in mat_b:
    print(n)

result = [[0 for i in range(column)] for i in range(rows)]

for i in range(rows):
    for j in range(column):
        result[i][j] = mat_a[i][j] + mat_b[i][j]

print("Sum of two Matrices is : ")
for r in result:
    print(r)
