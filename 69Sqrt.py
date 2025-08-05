class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while i*i <= x:
            if i*i == x:
                return i
            i+=1
        return i-1
    

x = int(input())
s = Solution()
print(s.mySqrt(x))
