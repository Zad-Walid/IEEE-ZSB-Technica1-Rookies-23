
l =[]

res = []

for j in range(3):

    a = list(map(int, input().split()))

    l.append(a)

if(l[0][0] + l[0][1] + l[1][0]) % 2 == 0:

    res.append("1")

else:

    res.append("0")

if(l[0][0] + l[0][1] + l[0][2]+l[1][1]) % 2 == 0:

    res.append("1")

else:

    res.append("0")

if(l[0][1] + l[0][2] + l[1][2]) % 2 == 0:

    res.append("1")

else:

    res.append("0")

if(l[0][0] + l[1][0] + l[1][1]+l[2][0]) % 2 == 0:

    res.append("1")

else:

    res.append("0")

if(l[0][1] + l[1][0] + l[1][1]+l[1][2]+l[2][1]) % 2 == 0:

    res.append("1")

else:

    res.append("0")

if(l[0][2] + l[1][1] + l[1][2]+l[2][2]) % 2 == 0:

    res.append("1")

else:

    res.append("0")

if(l[1][0] + l[2][0]+l[2][1]) % 2 == 0:

    res.append("1")

else:

    res.append("0")

if(l[2][2] + l[1][1] + l[2][1]+l[2][0]) % 2 == 0:

    res.append("1")

else:

    res.append("0")

if(l[2][1] + l[1][2]+l[2][2]) % 2 == 0:

    res.append("1")

else:

    res.append("0")

r1 = "".join(res[:3])

r2 = "".join(res[3:6])

r3 = "".join(res[6:9])

print(r1)

print(r2)

print(r3)