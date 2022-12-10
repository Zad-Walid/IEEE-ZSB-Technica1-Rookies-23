class DetectSquares:

    def __init__(self):
        self.cntPoints = Counter()

    def add(self, point: list[int]) -> None:
        self.cntPoints[tuple(point)] += 1

    def count(self, point: list[int]) -> int:
        ans = 0
        x1, y1 = point
        for (x3, y3), cnt in self.cntPoints.items():
            if abs(x1 - x3) == 0 or abs(x1 - x3) != abs(y1 - y3):
                continue
            ans += cnt * self.cntPoints[(x1, y3)] * self.cntPoints[(x3, y1)]
        return ans

