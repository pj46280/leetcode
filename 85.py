class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * (cols+1)
        area = 0

        for row in matrix:
            for i in range(cols):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0

            stack = [-1]
            for i in range(cols+1):
                while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                    h = heights[stack.pop()]
                    left = stack[-1]
                    right = i
                    w = right - left - 1
                    area = max(area, w*h)
                stack.append(i)

        return area
