class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        div = 1
        while x >= div * 10:
            div = div * 10

        while x:
            a, b = int(x/div), x%10
            if a != b:
                return False
            x = (x%div) // 10
            div = div / 100

        return True

x = int(input())
s = Solution()
print(s.isPalindrome(x))
