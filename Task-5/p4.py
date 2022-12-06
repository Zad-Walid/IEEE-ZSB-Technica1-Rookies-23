num = int(input("enter num"))

def x(num):
    i = 2
    p_factors = []
    while i * i <= num:
        if num % i == 0:
            p_factors.append(i)
            num //= i
        else:
            i += 1

    if num > 1:
        p_factors.append(num)

    return p_factors

print(x(num))