import random
num = random.randint(100,999)
print(num)
num = [int(x) for x in str(num)]
com_num = input("enter 3 digit number \n")
com_num = [int(x) for x in str(com_num)]
print (com_num)
hit = 0
miss = 0
for i in range(0,3):
    if num[i] == com_num[i]:
        i = i + 1
        hit = hit + 1
    elif ((num[0] == com_num[1] or com_num [2]) or (num[1] == com_num[0] or com_num [2]) or (num[2] == com_num[0] or com_num [1])):
        miss = miss + 1

print(hit ,"hits")
print (miss , "misses")