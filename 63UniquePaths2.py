class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        hashMap = {}
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        hashMap[(m-1, n-1)] = 1

        def dfs(i, j):
            if i == m or j == n or obstacleGrid[i][j] == 1:
                return 0
            if (i, j) in hashMap:
                return hashMap[(i, j)]

            hashMap[(i, j)] = dfs(i+1, j) + dfs(i, j+1)
            return hashMap[(i, j)]

        return dfs(0, 0)
        
