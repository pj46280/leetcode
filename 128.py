class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for n in nums:
            # new sequence
            if (n-1) not in nums:
                seq = 1
                m = n + 1
                while m in nums:
                    seq += 1
                    m += 1

                res = max(res, seq)

        return res
            


