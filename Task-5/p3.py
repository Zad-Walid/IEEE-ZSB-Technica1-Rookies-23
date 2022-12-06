num = input("enter number")

def equal_one(n):
  x  = []
  while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in x:
            return False
        x.append(n)
  return True

if equal_one(num) :
    print("true")
else:
    print("false")

