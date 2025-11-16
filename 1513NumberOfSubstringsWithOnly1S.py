class Solution:
    def numSub(self, s: str) -> int:
        MOD = (10**9 + 7)
        count = 0
        res = 0

        for ele in s:
            if ele == "1":
                count += 1
            else:
                res += count * (count + 1) // 2
                count = 0
        
        res += count * (count + 1) // 2

        return res % MOD
        
