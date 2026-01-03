class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10**9 + 7

        p1 = 6
        p2 = 6

        for i in range(1, n):
            _p1 = (p1*3 + p2*2) % mod
            _p2 = (p1*2 + p2*2) % mod
            p1 = _p1
            p2 = _p2

        return (p1+p2) % mod

