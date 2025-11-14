class Solution:
    def maxOperations(self, s: str) -> int:
        res = 0
        count = 0 if s[0] == '0' else 1

        for i in range(1, len(s)):
            if s[i] == '0' and s[i-1] == '1':
                res += count
            else:
                count += 1 if s[i] == '1' else 0

        return res
