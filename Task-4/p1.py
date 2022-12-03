print("enter n & k \n")
lst1 = list(map(int,input().split()))
k = lst1[1]
print("enter n int")
lst2 = list(map(int,input().split()))

map = {}
for i in range(len(lst2)):
    if lst2[i] in map:
        map[lst2[i]] += 1
    else:
        map[lst2[i]] = 1

s = (sorted(map.keys(),key= map.get , reverse= True)[:k])
print(s)
