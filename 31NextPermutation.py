class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j-=1
            nums[i], nums[j] = nums[j], nums[i]
        l, r = i+1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1

        return nums

# nums: 9 2 4 1 5
# nums: 2 7 6 5 4
# nums = [1,2,3]
# nums = [2,3,1]
# nums = [3,2,1]
# nums = [1, 3, 5, 4, 2]
nums = [4, 3, 2, 5, 4, 1, 3]
s = Solution()
print(s.nextPermutation(nums))

