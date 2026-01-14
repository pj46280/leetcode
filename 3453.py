class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def getArea(target):
            topArea, botArea = 0, 0
            for x, y, l in squares:
                top_limit, bot_limit = y+l, y
                if bot_limit <= target <= top_limit:
                    topArea += (top_limit - target) * l
                    botArea += (target - bot_limit) * l
                elif target < bot_limit:
                    topArea += l**2
                elif target > top_limit:
                    botArea += l**2

            return topArea - botArea

        lo, hi = inf, 0

        for x, y, l in squares:
            lo = min(lo, y)
            hi = max(hi, y+l)

        while (hi - lo) > 10**(-5):
            mid = (lo + hi) / 2
            d = getArea(mid)
            if d > 0:
                lo = mid
            else:
                hi = mid

        return hi
                


