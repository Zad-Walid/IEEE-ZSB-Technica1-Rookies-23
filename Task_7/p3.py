class Solution:
    def kClosest(self, points):
        answer = []
        min_dis = 0
        heapq.heapify(answer)
        for pt in points:
           dis = pt[0]**2 + pt[1]**2
           heapq.heappush(answer, (-dis, pt))
           if len(answer) > k:
               heapq.heappop(answer)

        return [y for x, y in answer]
