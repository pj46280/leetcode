class Solution:
    def generateMatrix(self, n):
        matrix = [[0]*n for j in range(n)]
        top, bottom = 0, n-1
        left, right = 0, n-1

        counter = 1
        while top <= bottom and left <= right:
            for i in range(left, right+1):
                matrix[top][i] = counter
                counter += 1
            top += 1

            for i in range(top, bottom+1):
                matrix[i][right] = counter
                counter += 1
            right -= 1

            k = right
            while k > left-1 and top <= bottom:
                matrix[bottom][k] = counter
                counter += 1
                k -= 1
            bottom -= 1

            k = bottom
            while k > top-1 and left <= right:
                matrix[k][left] = counter
                counter += 1
                k -= 1
            left += 1

        return matrix



s = Solution()
print(s.generateMatrix(3))

