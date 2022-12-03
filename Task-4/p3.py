arr = list(map(int,input().split()))

p_index = 0
c_index = 0

def min_distance(arr):

    map = dict()
    min_distance = 10 ** 9

    for i in range(len(arr)):

        if arr[i] in map:
            c_index = i

            p_index = map[arr[i]]

            min_distance = min((c_index - p_index), min_distance)


        map[arr[i]] = i

    if min_distance == 10**9:
        return -1
    return min_distance

print(min_distance(arr))