class Solution:
    def lastStoneWeight(self, st) :

      if len(st) ==0:
         return 0
      if len(st) == 1:
         return 1
      while len(st)>1:
         st.sort()
         s1,s2=st[-1],st[-2]
         if s1==s2:
            st.pop(-1)
            st.pop(-1)
         else:
            s1 = abs(s1-s2)
            st.pop(-1)
            st[-1] = s1
      if len(st):
         return st[-1]
      return 0
st1 = Solution()
print(st1.lastStoneWeight([2,7,4,1,6,1]))