class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        mn = inf
        neg = 0
        res = 0

        for i in range(n):
            for j in range(m):
                cur = matrix[i][j]
                if cur <= 0:
                    neg += 1
                mn = min(mn, abs(cur))
                res += abs(cur)

        return res if neg%2 == 0 else res - (2*mn)

