class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        res = 0

        for i in range(n):
            for j in range(i+1, n):
                # i-1 = first, i = second
                xl1, yb1 = bottomLeft[i]
                xr1, yt1 = topRight[i]
                xl2, yb2 = bottomLeft[j]
                xr2, yt2 = topRight[j]

                if (xl2 < xr1 and xr2 > xl1) and (yb2 < yt1 and yt2 > yb1):
                    left = max(xl1, xl2)
                    right = min(xr1, xr2)
                    top = min(yt1, yt2)
                    bot = max (yb1, yb2)
                    res = max(min((right - left), (top-bot)) ** 2, res)

        return res


