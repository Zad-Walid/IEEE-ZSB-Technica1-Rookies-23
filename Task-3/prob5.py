n ,m = map(int, input().split())
arr = list(map(int, input().split()))

hasStation = [0] * n
for city in arr:
    hasStation[city] = 1
dist, max_dist = 0, min(arr)

for city in range(n):
    if hasStation[city] == 1:
        max_dist = max((dist + 1) // 2, max_dist)
        dist = 0

    else:
        dist += 1
print(max(max_dist, dist))