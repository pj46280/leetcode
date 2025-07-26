class Solution:
    def romanToInt(self, s: str) -> int:
        # 19 -> XIX
        hashMap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        n=0
        for i in range(len(s)):
            if (i+1) < len(s) and hashMap[s[i]] < hashMap[s[i+1]]:
                n -= hashMap[s[i]]
            else:
                n += hashMap[s[i]]

        # while True:
        #     if i == len(s) - 1:
        #         a, b = s[i-1], s[i]
        #         if hashMap[a] >= hashMap[b]:
        #             n += hashMap[b]
        #         break
        #     a, b = s[i], s[i+1]
        #     if hashMap[b] > hashMap[a]:
        #         n += hashMap[b] - hashMap[a]
        #     else:
        #         n += hashMap[a]
        #     print(n)
        #     i+=1

        return n

string = input()
s = Solution()
print(s.romanToInt(string))
