class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        prev, current = 0, 1
        while n:
            prev, current = current, prev+current
            n-=1

        return current

n = int(input())
s = Solution()
print(s.climbStairs(n))
