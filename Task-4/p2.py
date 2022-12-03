print("enter s1 & s2")
s1 = input()
s2 = input()


def check_perm(s1, s2):

    size = len(s1)

    for i in range(len(s2)):

        w = s2[i:i + size]

        if is_perm(s1, w):
            return True

    return False


def is_perm(s, w):

    if len(s) != len(w):
        return False
    if s == w:
        return True

    from collections import Counter

    s1 = Counter(s)
    t1 = Counter(w)

    return s1 == t1

print(check_perm(s1,s2))

