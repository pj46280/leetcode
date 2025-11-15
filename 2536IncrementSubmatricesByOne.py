class Solution:
    def rangeAddQueries(self, n, queries):
        diff = [[0] * (n+1) for _ in range(n+1)]
        
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2+1] -= 1
            diff[r2+1][c1] -= 1
            diff[r2+1][c2+1] += 1

        mat = [[0]*n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                top = 0 if r==0 else mat[r-1][c]
                left = 0 if c==0 else mat[r][c-1]
                top_left = 0 if r==0 or c==0 else mat[r-1][c-1]
                mat[r][c] = diff[r][c] + top + left - top_left

        return mat

n = 3
queries = [[1,1,2,2],[0,0,1,1]]

s = Solution()
print(s.rangeAddQueries(n, queries))
