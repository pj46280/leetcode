class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p
        if target == 0: return 0
        prefix = 0
        prefixSum = {0: -1}
        res = len(nums)

        for i in range(len(nums)):
            prefix = (prefix + nums[i]) % p
            needed = (prefix - target + p) % p
            if needed in prefixSum:
                res = min(res, i - prefixSum[needed])
            prefixSum[prefix] = i

        return res if res < len(nums) else -1

