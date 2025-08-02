class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) >= len(needle):
            for i in range(len(haystack)):
                if (len(needle) <= len(haystack[i:])) and haystack[i:i+len(needle)] == needle:
                    return i
        else:
            return -1
        return -1

# 01234567 01234 0123456
# haystack stack stacked


haystack, needle = input().split()
s = Solution()
print(s.strStr(haystack, needle))
