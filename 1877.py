class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        res = -inf
        nums.sort()
        for i in range(len(nums)):
            res = max(res, nums[i]+nums[-i-1])
            
        return res
