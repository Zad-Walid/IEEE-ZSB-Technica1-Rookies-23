print("enter numbers")
numbers = list(map(int,input().split()))
print(len(numbers))
def plus (numbers):
    num = 0
    for i in range(len(numbers)):
    	num += numbers[i] * pow(10, (len(numbers)-1-i)) #[3,1,4,2] 3 * 10 ^ (4-1-0) = 3000
    return [int(i) for i in str(num+1)]

print(plus(numbers))