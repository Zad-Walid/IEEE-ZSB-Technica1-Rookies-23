t = int(input ())
n = int(input())
sum = 0
ans = 0

while (t > 0):
    a = int(input())
    sum = (86400 - a) + sum;
    ans = ans + 1
    if (n <= sum):
     break;
print(ans)
