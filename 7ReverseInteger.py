import math
class Solution:
    def reverse(self, x: int) -> int:
        MAX, MIN = 2147483647, -2147483648
        k, i = 10, 0
        while (x // k) > 0:
            i += 1
            k *= 10

        n, m = 0, 10**i
        for _ in range(i):
            # n += x%10 * m
            n += int(math.fmod(x, 10)) * m
            x = x // 10
            m = m // 10

        if (x > MAX//10 or (x == MAX//10 and n >= MAX%10)):
            return 0
        if (n < MIN//10 or (n == MAX//10 and x <= MIN%10)):
            return 0
        n = n*10 + x
        return n


n = int(input())
s = Solution()
print(s.reverse(n))
