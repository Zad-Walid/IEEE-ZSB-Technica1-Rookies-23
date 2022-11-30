
size = int(input("enter integer number \n"))
matrix = [[int(input()) for c in range (size)] for r in range(size)]
print (matrix)

sum1 = 0
for i in range (size):
    for j in range (size):
        if(i == j):
            sum1 += matrix[i][j]
sum2 = 0
for i in range(size):
    for j in range (size):
        if (i == size - j -1):
            sum2 += matrix[i][j]

diff = abs(sum2-sum1)
print(diff)