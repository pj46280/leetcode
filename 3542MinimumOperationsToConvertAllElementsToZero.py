class Solution:
    def minOperations(self, nums: List[int]) -> int:
        segments = 0
        stack = []

        for n in nums:
            while stack and stack[-1] > n:
                stack.pop()

            if n == 0:
                continue

            if not stack or n != stack[-1]:
                segments += 1
                stack.append(n)

        return segments
