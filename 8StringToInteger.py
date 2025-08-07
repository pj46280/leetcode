class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        sign = -1 if s[0] == "-" else 1
        if s[0] in {'-', '+'}:
            s = s[1:]

        res = 0
        for c in s:
            if not c.isdigit():
                break
            res = res*10 + int(c)
            if sign*res <= -2**31:
                return -2**31
            if sign*res >= 2**31 - 1:
                return 2**31 - 1

        return sign*res

# +042
# -042
# -+042
# -0c42
string = input()
s = Solution()
print(s.myAtoi(string))
