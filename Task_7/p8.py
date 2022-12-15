


s = str(input())
l = len(s)
s2 = []
i=0
while i < (l):
       if (s[i] == '.'):
          s2.append('0')
       elif (s[i] == '-' and s[i+1] == '.'):
          s2.append('1')
          i = i+1
       elif (s[i] == '-' and s[i+1] == '-'):
          s2.append('2')
          i = 1+i
       i = i+1
print (''.join(s2))

