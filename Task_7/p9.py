
s = int(input ())
while(True):
    s = s +1
    a = int(s / 1000)
    b = int(s / 100 % 10)
    c = int(s / 10 % 10)
    d = int(s % 10)
    if (a != b and a != c and a != d and b != c and b != d and c != d):
        break;
print(s)