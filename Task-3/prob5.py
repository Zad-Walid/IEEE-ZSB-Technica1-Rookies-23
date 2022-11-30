n ,m = map(int, input().split())
arr = list(map(int, input().split()))

station_t = [0] * n
for c in arr:
    station_t[c] = 1
dist, max_dist = 0, min(arr)

for c in range(n):
    if station_t[c] == 1:
        max_dist = max((dist + 1) // 2, max_dist)
        dist = 0

    else:
        dist += 1
print(max(max_dist, dist))