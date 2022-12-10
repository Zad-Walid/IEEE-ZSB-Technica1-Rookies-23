
def findDigits(n):
    list_x = []
    s = str(n)
    for i in s:
        if (int(i) != 0 and n % int(i) == 0):
            list_x.append(1)
    return (sum(list_x))


if __name__ == '__main__':


    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = print(findDigits(n))




