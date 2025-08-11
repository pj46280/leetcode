class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if pattern == ".*":
            return True

# abb
# ab
# aab

string, pattern = input().split()
s = Solution()
print(s.isMatch(string, pattern))
