class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        cur = 0
        res = []
        for num in nums:
            cur = (cur * 2 + num) % 5
            res.append(cur == 0)

        return res
