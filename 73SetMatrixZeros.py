class Solution:
    # def setZeroes(self, matrix: List[List[int]]) -> None:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    l.append((i,j))

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i,j) in l:
                    row, col = (0, 0)
                    while row < len(matrix):
                        matrix[row][j] = 0
                        row += 1
                    while col < len(matrix[0]):
                        matrix[i][col] = 0
                        col += 1

        return matrix
        

# matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix = [[0,1,2,0],[3,4,5,2],[0,3,1,0]]
s = Solution()
matrix = s.setZeroes(matrix)

for row in matrix:
    print(row)

