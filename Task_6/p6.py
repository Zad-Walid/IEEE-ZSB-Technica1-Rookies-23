def circularArrayRotation(a, k, queries):
    # Write your code here
    q_list = []
    for i in range(k):
        a.insert(0,a[-1])
        a.pop()
    for b in queries:
        q_list.append(a[b])
    return q_list

if __name__ == '__main__':
  

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = print(circularArrayRotation(a, k, queries))



