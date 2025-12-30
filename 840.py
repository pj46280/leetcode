class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0

        def is_valid(i, j):
            nums = set()
            for a in range(i-2, i+1):
                for b in range(j-2, j+1):
                    if grid[a][b] in nums: return False
                    nums.add(grid[a][b])
            
            d1 = grid[i-2][j-2] + grid[i-1][j-1] + grid[i][j]
            d2 = grid[i-2][j] + grid[i-1][j-1] + grid[i][j-2]

            if d1 != d2: return False

            for r in range(i-2, i+1):
                if grid[r][j-2] + grid[r][j-1] + grid[r][j] != d1: return False
            for c in range(j-2, j+1):
                if grid[i-2][c] + grid[i-1][c] + grid[i][c] != d1: return False

            return nums == set(range(1, 10))

        for i in range(2, n):
            for j in range(2, m):
                if is_valid(i, j):
                    res += 1
        return res

