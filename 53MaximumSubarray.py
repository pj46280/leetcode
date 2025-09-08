'''
class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    def maxSubArray(self, nums):
        # incase current_sum < 0 start = i
        start = i = 0
        stop = i
        max_sum = current_sum = 0
        for i in range(len(nums)):
            if current_sum < 0:
                start = i
                current_sum = 0
            current_sum += nums[i]
            if current_sum > max_sum:
                max_sum = current_sum
                stop = i

        return nums[start:stop+1]

class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    def maxSubArray(self, nums):
        # incase current_sum < 0 start = i
        max_sum = current_sum = 0
        for i in range(len(nums)):
            if current_sum < 0:
                current_sum = 0
            current_sum += nums[i]
            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # incase current_sum < 0 start = i
        max_sum = current_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum+nums[i])
            max_sum = max(current_sum, max_sum)

        return max_sum

# nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [1]
# nums = [5,4,-1,7,8]
nums = []
s = Solution()
print(s.maxSubArray(nums))

