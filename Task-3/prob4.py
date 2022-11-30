
total = int(input("enter total pages of the book \n"))
desired_p =int( input())

total /= 2
desired_p /= 2

print(min(desired_p, total - desired_p))