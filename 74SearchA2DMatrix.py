class Solution:
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n-1

        while l <= r:
            mid = (l + r) // 2
            row = mid // n
            col = mid % n
            val = matrix[row][col]

            if val == target:
                return True
            elif val > target:
                r = mid - 1
            else:
                l = mid + 1

        return False

        

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
s = Solution()
print(s.searchMatrix(matrix, 3))

