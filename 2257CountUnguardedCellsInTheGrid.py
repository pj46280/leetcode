class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [[0] * n for _ in range(m)]
        for r, c in guards: matrix[r][c] = 1
        for r, c in walls: matrix[r][c] = 2

        for r, c in guards:
            i = r-1
            while i >= 0 and matrix[i][c] != 1 and matrix[i][c] != 2:
                if matrix[i][c] == 0: matrix[i][c] = 3
                i -= 1
            
            i = r+1
            while i < m and matrix[i][c] != 1 and matrix[i][c] != 2:
                if matrix[i][c] == 0: matrix[i][c] = 3
                i += 1
            
            j = c-1
            while j >= 0 and matrix[r][j] != 1 and matrix[r][j] != 2:
                if matrix[r][j] == 0: matrix[r][j] = 3
                j -= 1

            j = c+1
            while j < n and matrix[r][j] != 1 and matrix[r][j] != 2:
                if matrix[r][j] == 0: matrix[r][j] = 3
                j += 1

        return sum(matrix[i][j] == 0 for i in range(m) for j in range(n))

            
        
# m = 3
# n = 3
# guards = [[1,1]]
# walls = [[0,1],[1,0],[2,1],[1,2]]

m = 4
n = 6
guards = [[0,0],[1,1],[2,3]]
walls = [[0,1],[2,2],[1,4]]

s = Solution()
print(s.countUnguarded(m, n, guards, walls))
