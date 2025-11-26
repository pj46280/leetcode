class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        cache = [[[-1]*k for _ in range(COLS)] for _ in range(ROWS)]
        MOD = 10**9 + 7

        def traverse(r, c, remainder):
            if r == ROWS-1 and c == COLS-1:
                remainder = (remainder + grid[r][c]) % k
                return 0 if remainder else 1
            if r == ROWS or c == COLS:
                return 0
            if cache[r][c][remainder] > -1:
                return cache[r][c][remainder]
            cache[r][c][remainder] = (
                traverse(r+1, c, (remainder + grid[r][c])%k)%MOD + 
                traverse(r, c+1, (remainder + grid[r][c])%k)%MOD
            )%MOD

            return cache[r][c][remainder]

        return traverse(0, 0, 0)

            
