class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # s = a
        if len(s) <= 1:
            return len(s)

        ptr1, ptr2 = 0, 1
        string = ""
        current = "" + s[ptr1]
        while ptr2 < len(s):
            i = ptr2
            while s[ptr2] in current:
                current = current[i:]
                ptr2 += 1
                i += 1
            else:
                current += s[ptr2]
            ptr2 += 1
            if len(current) > len(string):
                string = current

        return len(string)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        count = 0

        for right in range(len(s)):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1
            seen[s[right]] = right
            count = max(count, right - left + 1)

        return count


s = Solution()
l = s.lengthOfLongestSubstring(input())
print(l)

