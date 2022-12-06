
def max_heapify(a,k):
    l = left(k)
    r = right(k)
    if l < len(a) and a[l] > a[k]:
        largest = l
    else:
        largest = k
    if r < len(a) and a[r] > a[largest]:
        largest = r
    if largest != k:
        a[k], a[largest] = a[largest], a[k]
        max_heapify(a, largest)

def left(k):
    return 2 * k + 1

def right(k):
    return 2 * k + 2

def build_max_heap(a):
    n = int((len(a)//2)-1)
    for k in range(n, -1, -1):
        max_heapify(a,k)

a = list(map(int,input().split()))
build_max_heap(a)
print(a)