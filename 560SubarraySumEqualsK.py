class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        d = {0:1}
        s = 0

        for n in nums:
            s += n
            target = s - k
            if target in d:
                res += d[target]
            d[s] = d[s]+1 if s in d else 1

        return res

