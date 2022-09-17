import numpy as np
m=int(input("Row:"))
n=int(input("Column:"))
matrix1=[]
for row in range(m):
    for col in range(n):
         matrix1=[[row*col for col in range(n)] for row in range(m)]
print(matrix1)

# or using numpy
matrix2=np.empty((m,n))
for row1 in range(m):
    for col1 in range(n):
        matrix2[row1,col1]=row1*col1
# matrix2.reshape(m,n)
print(matrix2)





