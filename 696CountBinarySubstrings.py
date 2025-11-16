class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # 001110011
        # 0011010011
        prev = 0
        count = 1
        res = 0

        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                count += 1
            else:
                res += min(count, prev)
                prev = count
                count = 1

        return res + min(count, prev)

#string = "001110011"
#string = "00110011"
string = "10101"
s = Solution()
print(s.countBinarySubstrings(string))

