'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) >= len(needle):
            for i in range(len(haystack)):
                if (len(needle) <= len(haystack[i:])) and haystack[i:i+len(needle)] == needle:
                    return i
        else:
            return -1
        return -1
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "": return 0
        lps = [0] * len(needle)
        j, i = (0, 1)

        while i < len(needle):
            if (needle[j] == needle[i]):
                lps[i] = j + 1
                i += 1
                j += 1
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    lps[i] = 0
                    i += 1

        i, j = (0, 0) 
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
            if j == len(needle):
                return i - len(needle)

        return -1


# 01234567 01234 0123456
# haystack stack stacked


haystack, needle = input().split()
s = Solution()
print(s.strStr(haystack, needle))
