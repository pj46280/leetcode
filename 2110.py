class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        prev = 1
        res = 1

        for i in range(1, len(prices)):
            if prices[i] == prices[i-1] - 1:
                prev += 1
            else:
                prev = 1
            res += prev

        return res

