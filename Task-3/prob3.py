
no_b = int(input("enter number of bottles"))
matrix = []
for i in range (no_b):
    v_c = input().split()
    matrix.append(v_c)
print(matrix)
sum_vol = 0
sum_cap = 0
for i in range (no_b):
    for j in range (no_b):
        sum_vol += int(matrix[j][0])
        sum_cap += int(matrix[j][1])

if (sum_vol % 2 == 0 )and (sum_vol <= sum_cap):
            print("yes")
else:
            print("no")

