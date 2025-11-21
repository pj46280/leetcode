class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        counter = 0
        seen = set()
        for i in range(len(s)):
            if s[i] in seen:
                continue
            d = {}
            first, last = i, i
            for j in range(i+1, len(s)):
                if s[j] == s[i]:
                    last = j

            if first != last:
                for k in range(first+1, last):
                    if s[k] not in d: 
                        counter += 1
                    d[s[k]] = 1

            seen.add(s[i])

        return counter
