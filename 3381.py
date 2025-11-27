class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = [float("inf")] * k
        prefixSum[0] = 0
        res = float("-inf")
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            length = i + 1
            prefix_remainder = length % k
            res = max(res, total - prefixSum[prefix_remainder])
            prefixSum[prefix_remainder] = min(prefixSum[prefix_remainder], total)

        return res

