import math
class Solution:
    def reverse(self, x: int) -> int:
        MAX, MIN = 2147483647, -2147483648

        n = 0
        while x:
            m = int(math.fmod(x, 10))
            x = int(x/10)

            if (n > MAX//10) or (n == MAX//10 and m >= MAX%10):
                return 0
            if (n < MIN//10) or (n == MIN//10 and m <= MIN%10):
                return 0
            n = n*10 + m


        return n


n = int(input())
s = Solution()
print(s.reverse(n))
