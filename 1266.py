class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total = 0
        cx, cy = points[0][0], points[0][1]

        for i in range(1, len(points)):
            x, y = points[i][0], points[i][1]
            a, b = abs(x-cx), abs(y-cy)
            total += max(a, b)
            cx, cy = x, y

        return total

