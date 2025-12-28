class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0

        for row in grid:
            n = len(row)
            start = n
            l, r = 0, n-1

            while l <= r:
                mid = (l+r) // 2
                if row[mid] < 0:
                    start = mid
                    r = mid - 1
                else:
                    l = mid + 1

            res +=  n - start

        return res
