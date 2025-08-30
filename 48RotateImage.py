class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        row=0
        while row < len(matrix):
            l, r = 0, len(matrix[row]) - 1
            while l < r:
                matrix[row][l], matrix[row][r] = matrix[row][r], matrix[row][l]
                l += 1
                r -= 1
            row += 1

        return matrix

'''
# 1. Transpose the matrix
1 2 3
4 5 6
7 8 9

1 4 7
2 5 8
3 6 9

7 4 1
8 5 2
9 6 3
'''

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
s = Solution()
print(s.rotate(matrix))

