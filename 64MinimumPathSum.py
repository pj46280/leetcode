class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        hashMap = {}
        
        def minPath(i, j):
            if (i, j) in hashMap:
                return hashMap[(i, j)]

            if i == 0 and j == 0:
                return grid[i][j]
                
            if i == 0:
                hashMap[(i, j)] = grid[i][j] + minPath(i, j-1)
            elif j == 0:
                hashMap[(i, j)] = grid[i][j] + minPath(i-1, j)
            else:
                hashMap[(i, j)] = grid[i][j] + min(minPath(i-1, j), minPath(i, j-1))

            return hashMap[(i, j)]

        return minPath(m-1, n-1)


